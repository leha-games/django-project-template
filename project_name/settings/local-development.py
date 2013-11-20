"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .base import BASE_DIR


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# INTERNAL_IPS = ('127.0.0.1')


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, '../db', 'db.sqlite3'),                      # Or path to database file if using sqlite3.
    }
}


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False



# Third-party apps settings

# easy-thumbnails

THUMBNAIL_DEBUG = True
