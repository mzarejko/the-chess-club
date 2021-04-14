from .base import *
import os
from datetime import timedelta
from pathlib import Path
import django_heroku
import dj_database_url

'''
file is env for production!!
'''

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY= os.environ.get('SECRET_KEY') 
DEBUG = False 

ALLOWED_HOSTS = ['https://thechessclub.herokuapp.com']

# ASGI is for djnago channel
ASGI_APPLICATION = 'base.routing.application'
WSGI_APPLICATION = 'base.wsgi.application'

# connect with Heroku databas
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

# ASGI is for djnago channel
ASGI_APPLICATION = 'base.routing.application'
WSGI_APPLICATION = 'base.wsgi.application'

# lib for manage serve own static files, important for Heroku
INSTALLED_APPS += [
    "whitenoise.runserver_nostatic",
]

# add this middleware to base settings
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# this will automatically configure DATABASE and HOSTS 
django_heroku.settings(locals())
