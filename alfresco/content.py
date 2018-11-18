import requests
import base64
from django.conf import settings

def get_content_informations(nodeId, token):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/pdf' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
    
    results = []
   
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_NODES + "/" + nodeId, headers=headers)
        result = response.json()
        return result
    
    except :
        print("Error when querying the Alfresco API.")

def get_content_mimetype(nodeId, token):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/pdf' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
    
    results = []
   
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_NODES + "/" + nodeId, headers=headers)
        result = response.json()
        return result['entry']['content']['mimeType']
    
    except :
        print("Error when querying the Alfresco API.")
    
        
def get_content(nodeId, token):
    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/pdf' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
    default_params = "content?attachment=false"

    try:
        response  = requests.get(settings.URL_CORE + settings.URL_NODES + "/" + nodeId + "/" + default_params, headers=headers)
        return response
    except :
        print("Error when querying the Alfresco API.")
    
    
    