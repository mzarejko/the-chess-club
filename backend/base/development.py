from .base import *
import os
from datetime import timedelta
from pathlib import Path
from decouple import config

'''
This file is for local development!!

django use decouple lib for important settings so it 
need .env file in the same falder as this file
'''
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY= 'dfefghjuwiwh345892hbf81Idio5lp@&YBKigw'
DEBUG = True

ALLOWED_HOSTS = [ '127.0.0.1', '172.16.238.11']

# page to redirect from backend
REDIRECT_PAGE = 'http://0.0.0.0:3000/reset-password/'

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
    EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
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
    EMAIL_HOST_USER=config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   ]

# ASGI is for djnago channel
ASGI_APPLICATION = 'base.routing.application'
WSGI_APPLICATION = 'base.wsgi.application'

# important for authentication
AUTH_USER_MODEL = 'accounts.User'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
