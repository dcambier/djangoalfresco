import json
import requests
import base64
from django.conf import settings

def count_sites(token):
    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
    
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_SITES + default_params, headers=headers)
        content = response.json()
        
        count = len(content['list']['entries'])
    except :
        print("Error when querying the Alfresco API.")
    return count

def count_tags(token):
    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
 
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_TAGS + default_params, headers=headers)
        content = response.json()
        count = len(content['list']['entries'])
    except :
        print("Error when querying the Alfresco API.")
    return count
    
def count_people(token):
    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
 
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_PEOPLE + default_params, headers=headers)
        content = response.json()
        count = len(content['list']['entries'])
    except :
        print("Error when querying the Alfresco API.")
    return count
        
def count_groups(token):
    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}
 
    try:
        response  = requests.get(settings.URL_CORE + settings.URL_GROUPS + default_params, headers=headers)
        content = response.json()   
        count = len(content['list']['entries'])
    except :
        print("Error when querying the Alfresco API.")
    return count     
    