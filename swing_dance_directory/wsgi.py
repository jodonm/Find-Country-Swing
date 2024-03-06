import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swing_dance_directory.settings')

application = get_wsgi_application()

