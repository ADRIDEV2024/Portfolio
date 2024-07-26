import os
from django.core.asgi import get_asgi_application
import daphne

# This code initializes my web application with ASGI settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Language.settings')
application = get_asgi_application()
