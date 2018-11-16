# DjangoAlfresco
Django Alfresco AdminLTE is REST Client for [Alfresco Remote API](https://github.com/Alfresco/alfresco-remote-api) based on Django with [AdminLTE Theme](https://adminlte.io/).

# Requirements
Django Alfresco works thanks to:

 - Python 3.7.0+ 
 - Django 2.1.3+ 
 - requests 
 - django-tables2 
 - django_pdb
 - django-debug-toolbar

If you want full support then install dependencies make sure to install these packages prior to installation in your environment:

    pip install requests
    pip install django-tables2
    pip install django_pdb
    pip install django-debug-toolbar

## Features (16/11/2018)
POST - Login Authentication
https://api-explorer.alfresco.com/api-explorer/#!/authentication/createTicket
STORE user informations in 
![enter image description here](https://picasaweb.google.com/110205653017955609271/6624536636932301601#6624536639955830498)
GET - List Sites 
GET - List Groups
GET - List People
GET - List Tags

## Database

User Informations are stored in database SQLite. (sqlite3.db)
Change database in settings.py 

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'sqlite3.db',                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

## Alfresco

Change Alfresco settings in settings.py
    
    PROTOCOL           = "http://"
    SERVER             =  "192.168.0.107" 
    PORT               = "8080"
    VERSION            = "1"
   
    USER_LOGIN    = "admin"
    USER_PASSWORD = "admin"



## Execute server

    python manage.py runserver

