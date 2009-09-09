import os

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1')

ADMINS = (
            ('admin', 'admin@some.mail'),
         )
MANAGERS = ADMINS

DEFAULT_CHARSET = 'UTF-8'

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'mydatabase'        # Or path to database file if using sqlite3.
DATABASE_USER = 'root'              # Not used with sqlite3.
DATABASE_PASSWORD = 'password'      # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'Europe/Kiev'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static/')

MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'secret_key'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    #"django.core.context_processors.debug",
    "django.core.context_processors.media"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sessions',
)

try:
    from settings_local import *
except ImportError:
    pass