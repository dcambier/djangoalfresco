import requests
import json
import base64

from requests.auth import HTTPBasicAuth
from django.shortcuts import render
from django.conf import settings
from django.template.context import RequestContext
from alfresco.search import run_query

############################################
# PAGES
############################################
def index(request):
    return render(request, "adminlte/index.html", 
    {'title': ''})

def sites(request):
    if request.user.is_authenticated:
        password = request.user.password

    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(password, "utf-8"))}
 
    response  = requests.get(settings.URL_CORE + settings.URL_SITES + default_params, headers=headers)
    content = response.json()
        
    return render(request, 'adminlte/sites.html', {
        'status' : response.status_code,
        'title' : 'List of Sites',
        'sites' : content['list']['entries'],
    })

def groups(request):
    if request.user.is_authenticated:
        password = request.user.password

    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(password, "utf-8"))}
 
    response  = requests.get(settings.URL_CORE + settings.URL_GROUPS + default_params, headers=headers)
    content = response.json()
        
    return render(request, 'adminlte/groups.html', {
        'status' : response.status_code,
        'title' : 'List of Groups',
        'groups' : content['list']['entries'],
    })

def people(request):
    if request.user.is_authenticated:
        password = request.user.password

    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(password, "utf-8"))}
 
    response  = requests.get(settings.URL_CORE + settings.URL_PEOPLE + default_params, headers=headers)
    content = response.json()
        
    return render(request, 'adminlte/people.html', {
        'status' : response.status_code,
        'title' : 'List of People',
        'people' : content['list']['entries'],
    })    

def tags(request):
    if request.user.is_authenticated:
        password = request.user.password

    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(password, "utf-8"))}
 
    response  = requests.get(settings.URL_CORE + settings.URL_TAGS + default_params, headers=headers)
    content = response.json()
    
    return render(request, 'adminlte/tags.html', {
        'status' : response.status_code,
        'title' : 'List of Tags',
        'tags' : content['list']['entries'],
    })   
    
def search(request):
    if request.user.is_authenticated:
        password = request.user.password
        
    result_list = []
    
    if request.method == 'POST':
        query = request.POST['query'].strip()
        
        if query:
            result_list = run_query(query, password)
            
    return render(request, 'adminlte/search.html', {
        'result_list': result_list})
