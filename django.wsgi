import sys
import os
import os.path
from django.core.handlers.wsgi import WSGIHandler

def app(environ, start_response):
    sys.path.insert(0, os.path.dirname(__file__))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    handler = WSGIHandler()
    return handler(environ, start_response)

application = app