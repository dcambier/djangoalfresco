import requests
import json
import base64

from django.shortcuts import render
from django.conf      import settings
from django.http      import HttpResponse, JsonResponse
from alfresco.search  import run_query, run_query_cmis
from alfresco.content import get_content, get_content_informations, get_content_mimetype
from alfresco.count   import count_sites, count_tags, count_people, count_groups
from alfresco.utils   import percentage
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

############################################
# PAGES
############################################
def index(request):
    if request.user.is_authenticated:
        password = request.user.password
    
    # TODO : Token invalid, automatic logout + redirect
    # logout(request)
    # return HttpResponseRedirect("/admin/login")
    
    counter_sites  = count_sites(password)
    counter_tags   = count_tags(password)
    counter_people = count_people(password)
    counter_groups = count_groups(password)    
    
    percent_sites  = percentage(counter_sites, 100)
    percent_tags   = percentage(counter_tags, 100)
    percent_people = percentage(counter_people, 100)
    percent_groups = percentage(counter_groups, 100)
    
    result_list_last_documents = []
    query = "Select * from cmis:document ORDER BY cmis:creationDate DESC"
    result_list_last_documents = run_query_cmis(query, password, 10)
    
    return render(request, "adminlte/index.html", 
    {
        'build_page_title' : 'Alfresco Django',
        'count_sites' : counter_sites,
        'count_tags'  : counter_tags,
        'count_people': counter_people,
        'count_groups': counter_groups,
        'percent_sites': percent_sites,
        'percent_tags': percent_tags,
        'percent_people': percent_people,
        'percent_groups': percent_groups,
        'result_list': result_list_last_documents,
    })

def sites(request):
    if request.user.is_authenticated:
        password = request.user.password

    default_params = "?skipCount=0&maxItems=100"

    auth = bytes('Basic ', "utf-8")
    headers = {'Accept': 'application/json' , 'Authorization' : auth + base64.b64encode(bytes(password, "utf-8"))}
 
    response  = requests.get(settings.URL_CORE + settings.URL_SITES + default_params, headers=headers)
    content = response.json()
        
    return render(request, 'adminlte/sites.html', {
        'build_page_title' : 'Alfresco Django - Sites',
        'status' : response.status_code,
        'title' : 'List of Sites',
        'sites' : content['list']['entries'],
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
        'build_page_title' : 'Alfresco Django - Tags',
        'status' : response.status_code,
        'title' : 'List of Tags',
        'tags' : content['list']['entries'],
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
        'build_page_title' : 'Alfresco Django - People',
        'status' : response.status_code,
        'title' : 'List of People',
        'people' : content['list']['entries'],
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
        'build_page_title' : 'Alfresco Django - Groups',
        'status' : response.status_code,
        'title' : 'List of Groups',
        'groups' : content['list']['entries'],
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
        'build_page_title' : 'Alfresco Django - Search',
        'result_list': result_list})
    
def viewer(request, nodeId):
    if request.user.is_authenticated:
        password = request.user.password
    
    return render(request, 'adminlte/viewer.html', {
        'build_page_title' : 'Alfresco Django - Viewer',
        'nodeId' : nodeId})    
    
def content(request, nodeId):
    if request.user.is_authenticated:
        password = request.user.password
        
    content = get_content(nodeId, password)
    response = HttpResponse(content)
    mimetype = get_content_mimetype(nodeId, password)
    response['Content-Type'] = mimetype
    return response

def content_json(request, nodeId):
    if request.user.is_authenticated:
        password = request.user.password
        
    content = get_content_informations(nodeId, password)
    content = json.dumps(content, indent=4, sort_keys=True)
    
    response = HttpResponse(content)
    response['Content-Type'] = 'application/json'
    return response
    