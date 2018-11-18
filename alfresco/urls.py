from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'Django Alfresco'

urlpatterns = [
    path('', views.index, name='index'),
    path('sites', views.sites, name='sites'),
    path('groups', views.groups, name='groups'),
    path('people', views.people, name='people'),
    path('tags', views.tags, name='tags'),
    path('search', views.search, name='search'),
    url(r'^viewer/(?P<nodeId>[a-zA-Z0-9_-]+)$',views.viewer),
    url(r'^content/(?P<nodeId>[a-zA-Z0-9_-]+)$',views.content),
    url(r'^content_json/(?P<nodeId>[a-zA-Z0-9_-]+)$',views.content_json),
    
]