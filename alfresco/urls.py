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
]