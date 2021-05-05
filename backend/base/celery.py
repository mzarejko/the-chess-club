import os 
from celery import Celery
from . import development


if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.development')

if os.environ.get('GITHUB_WORKFLOW'):
    BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://172.16.238.13:6379')
else:
    BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('base')
app.config_from_object(development)
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL
