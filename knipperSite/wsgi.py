"""
WSGI config for knipperSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/root/SnelleKnipper')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knipperSite.settings')

application = get_wsgi_application()
