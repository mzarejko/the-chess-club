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

ALLOWED_HOSTS = ['the-chess-club-backend.herokuapp.com']

REDIRECT_PAGE = 'http://the-chess-club.herokuapp.com/reset-password/'

# ASGI is for djnago channel
ASGI_APPLICATION = 'base.routing.application'
WSGI_APPLICATION = 'base.wsgi.application'

# connect with Heroku databas
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_URL = '/static/media/'

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

EMAIL_HOST_USER=os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
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
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}


# this will automatically configure DATABASE and HOSTS 
django_heroku.settings(locals())
