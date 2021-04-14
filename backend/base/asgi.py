import os

from django.core.asgi import get_asgi_application
 
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.development')

application = get_asgi_application()
