"""
This is an example settings/local.py file.
These settings overrides what's in settings/base.py
"""

DEBUG = TEMPLATE_DEBUG = THUMBNAIL_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True


INTERNAL_IPS = ('127.0.0.1')


ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db/development.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False



