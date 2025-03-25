"""
WSGI config for transkritor project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transkritor.settings')

application = get_wsgi_application()
