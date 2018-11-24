import requests
import base64
from django.conf    import settings
from requests.auth  import HTTPBasicAuth

def post_ticket(username, password):
    headers = {
    'Accept': 'application/json', 
    'Content-Type' : 'application/json',
    }
    
    body = '{"userId":"' + username + '", "password":"' + password + '"}'
   
    try:
        response = requests.post(settings.URL_AUTHENTICATION + settings.URL_TICKETS, headers=headers, data=body, auth=HTTPBasicAuth(settings.USER_LOGIN, settings.USER_PASSWORD))
   
    except :
        response= None
        print("Error when querying the Alfresco Authentication API.")
        
    return response    

def get_ticket(token):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
    
    results = []
   
    try:
        response  = requests.get(settings.URL_AUTHENTICATION + settings.URL_TICKETS + "/-me-", headers=headers)
    
    except :
        response= None
        print("Error when querying the Alfresco Authentication API.")
    
    return response

    
        
    
    