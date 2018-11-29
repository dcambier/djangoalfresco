import requests
import base64
from django.conf    import settings
from requests.auth  import HTTPBasicAuth

def get_peoples(maxItems):

    headers = {'Accept': 'application/json'}
    default_params = '?skipCount=0&maxItems=100' + maxItems
    try:
        response = requests.get(settings.URL_CORE + settings.URL_PEOPLE + default_params, headers=headers, auth=HTTPBasicAuth(settings.USER_LOGIN, settings.USER_PASSWORD))
    
    except :
        response = None
        print("Error when querying the Alfresco Core API.")
    
    return response

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

def get_people_avatar(token, username):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}    
    try:
        print(settings.URL_CORE + settings.URL_PEOPLE + "/" + username + "/avatar?attachment=false&placeholder=true")
        response  = requests.get(settings.URL_CORE + settings.URL_PEOPLE + "/" + username + "/avatar?attachment=false&placeholder=true", headers=headers)
    
    except :
        response = None
        print("Error when querying the Alfresco Core API.")   
        
    return response  

def get_people_activities(token, username, maxItems):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}    
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_PEOPLE + "/" + username + "/activities?skipCount=0&maxItems=" + maxItems, headers=headers)
    
    except :
        response = None
        print("Error when querying the Alfresco Core API.")   
        
    return response  
    
    