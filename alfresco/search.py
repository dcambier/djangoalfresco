import json
import requests
import base64
from django.conf import settings

def run_query(search_terms, token):
    auth = bytes('Basic ', "utf-8")
    headers = {'Content-Type': 'application/json' , 'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(token, "utf-8"))}

    body = '{ "query" : { "query" : "' + search_terms + '"} }'
    results = []
    try:
        print(body)
        print(settings.URL_ROOT_SEARCH + settings.URL_SEARCH)
        response  = requests.post(settings.URL_ROOT_SEARCH + settings.URL_SEARCH , headers=headers, data=body)
        content = response.json()
        print(content)
        print(content['list']['entries'])
        for result in content['list']['entries']:
            results.append({
                'name'     :  result['entry']['name'], 
                'id'       :  result['entry']['id'], 
                'location' :  result['entry']['location']})
    except :
        print("Error when querying the Alfresco API.")
    
    return results
    