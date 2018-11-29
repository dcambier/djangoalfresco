from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

admin.site.site_header = 'Django Alfresco'

urlpatterns = [
    path('', views.index, name='index'),
    path('sites', views.sites, name='sites'),
    path('groups', views.groups, name='groups'),
    path('people', views.people, name='people'),
    path('tags', views.tags, name='tags'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    
    url(r'^avatar/(?P<userId>[a-zA-Z0-9_-]+)$',views.avatar),
        
    url(r'^viewer/(?P<nodeId>[a-zA-Z0-9_-]+)$',views.viewer),
    url(r'^content/(?P<nodeId>[a-zA-Z0-9_-]+)$',views.content),

    url(r'^content_json/(?P<nodeId>[a-zA-Z0-9_-]+)$',views.content_json),
    
    path('admin/login/', auth_views.LoginView.as_view(), name='login'),    
    path('admin/', views.index, name='index'),
    url(r'^admin/', admin.site.urls),    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

]
