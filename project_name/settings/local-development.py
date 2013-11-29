"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import BASE_DIR


INTERNAL_IPS = ('127.0.0.1')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, '../db', 'db.sqlite3'),                      # Or path to database file if using sqlite3.
    }
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False



# Third-party apps settings

# easy-thumbnails

THUMBNAIL_DEBUG = True
