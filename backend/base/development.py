from .base import *
import os
from datetime import timedelta
from pathlib import Path

'''
This file is for local development!!

django use decouple lib for important settings so it 
need .env file in the same falder as this file
'''
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY= 'dfefghjuwiwh345892hbf81Idio5lp@&YBKigw'
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '172.16.238.11']


# this parametrs are for CI/CD on gitchub actions
if os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'chessbase',
           'USER': 'owner',
           'PASSWORD': 'harnas',
           'HOST': 'db',
           'PORT': '5432',
        }
    }
else:
# this params are for local work, see that here is localhost
    DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'chessbase',
           'USER': 'owner',
           'PASSWORD': 'harnas',
           'HOST': 'localhost',
           'PORT': '5432',
        }
    }
    

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ASGI is for djnago channel
ASGI_APPLICATION = 'base.routing.application'
WSGI_APPLICATION = 'base.wsgi.application'




