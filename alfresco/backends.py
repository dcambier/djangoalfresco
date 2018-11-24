from __future__ import unicode_literals

import requests
import datetime
import logging
import time
import json
import sys

from django.conf                  import settings
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth          import get_user_model
from requests.auth                import HTTPBasicAuth
from alfresco.authentication      import post_ticket
from alfresco.people              import get_people


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

        response = post_ticket(username, password)
        token = response.json()

        if response.status_code == 201 :
            try: 
                response = get_people(username)

            except: informations = None

            informations = response.json()
           
            UserModel = get_user_model()

            if self.create_unknown_user:
                user, created = UserModel._default_manager.get_or_create(defaults={
                                    'email'        : informations['entry']['email'],
                                    'first_name'   : informations['entry']['firstName'],
                                    #'last_name'    : informations['entry']['lastName'],
                                    'password'     : token['entry']['id'],
                                    #'is_superuser' : is_superuser,
                                    'is_active'    : informations['entry']['enabled'],
                                    'is_staff'     : informations['entry']['capabilities']['isGuest'] == False,
                                    'last_login'   : datetime.datetime.now(),
                                    #'member_of' : data.get('memberOf', ''),
                                }, **{
                                    UserModel.USERNAME_FIELD:username,
                                })
                
                user.password = token['entry']['id'];
                
                is_superuser = 0
                if informations['entry']['capabilities']['isAdmin'] == True:
                    is_superuser = 1
                user.is_superuser = is_superuser     

                is_active = 0
                if informations['entry']['enabled'] == True:
                    is_active = 1
                user.is_active = is_active        
                
                try :          
                    user.last_name = informations['entry']['lastName']
                except KeyError:
                    user.last_name = ''
                    
                user.save()
                if created:
                    user = self.configure_user(user)
            else:
                try:
                    user = UserModel._default_manager.get_by_natural_key(username)
                except UserModel.DoesNotExist:
                    pass
        logger.debug( 'authenticate user {0}'.format(user) )
        return user

    def clean_username(self, username):
        return username

    def configure_user(self, user):
        return user