import requests
import base64
from django.conf    import settings
from requests.auth  import HTTPBasicAuth

def get_people(username):

    headers = {'Accept': 'application/json' , 'Content-Type' : 'application/json'}
   
    try:
        response = requests.get(settings.URL_CORE + settings.URL_PEOPLE + "/" + username, headers=headers, auth=HTTPBasicAuth(settings.USER_LOGIN, settings.USER_PASSWORD))
    
    except :
        response = None
        print("Error when querying the Alfresco Core API.")
    
    return response

def get_people_id(token, username):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}    
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_PEOPLE + "/" + username, headers=headers)
    
    except :
        response = None
        print("Error when querying the Alfresco Core API.")   
        
    return response    
    
    