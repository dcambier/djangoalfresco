from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth import get_user_model
import requests
from requests.auth import HTTPBasicAuth
import datetime
import logging
import time
import json
import sys

logger = logging.getLogger('django.auth.backends')

def no_check_cert():
    try:
        import ssl
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx
    except:
        return None

class RemoteAuthBackend(RemoteUserBackend):

    def authenticate(self, request, username=None, password=None):
        user = None
        token = None

        headers = {
        'Accept': 'application/json', 
        'Content-Type' : 'application/json',
        }

        body = '{"userId":"' + username + '", "password":"' + password + '"}'
        try: 
            response = requests.post(settings.URL_AUTHENTICATION + settings.URL_TICKETS, headers=headers, data=body, auth=HTTPBasicAuth(settings.USER_LOGIN, settings.USER_PASSWORD))
        except: token = None

        token = response.json()

        if response.status_code == 201 :
            try: 
                response = requests.get(settings.URL_CORE + settings.URL_PEOPLE + "/" + username, headers=headers, auth=HTTPBasicAuth(settings.USER_LOGIN, settings.USER_PASSWORD))
            except: informations = None

            informations = response.json()
           
            UserModel = get_user_model()

            if self.create_unknown_user:
                                              
                user, created = UserModel._default_manager.get_or_create(defaults={
                                    'email'        : informations['entry']['email'],
                                    'first_name'   : informations['entry']['firstName'],
                                    #'last_name'    : informations['entry']['lastName'],
                                    'password'     : token['entry']['id'],
                                    'is_superuser' : 1,
                                    'is_active'    : informations['entry']['enabled'],
                                    'is_staff'     : informations['entry']['capabilities']['isGuest'] == False,
                                    'last_login'   : datetime.datetime.now(),
                                    #'member_of' : data.get('memberOf', ''),
                                }, **{
                                    UserModel.USERNAME_FIELD:username,
                                })
                user.password = token['entry']['id'];
                user.save()
                if created:
                    user = self.configure_user(user)
                    user.password = token['entry']['id'];
                    user.save()
            else:
                try:
                    user = UserModel._default_manager.get_by_natural_key(username)
                    user.password = token['entry']['id'];
                    user.save()
                except UserModel.DoesNotExist:
                    pass
        logger.debug( 'authenticate user {0}'.format(user) )
        return user

    def clean_username(self, username):
        return username

    def configure_user(self, user):
        return user