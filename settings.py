import os
from os.path import abspath, dirname
from ConfigParser import ConfigParser

PROJECT_ROOT = dirname(abspath(__file__))

# This list is for values to be treated as strings
OVERRIDABLE_STRINGS = []
OVERRIDABLE_BOOLEANS = ['DEBUG',]
                        

# Django settings for codatimetric project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Michael Dales', 'mwd@camvine.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'codatimetricdb'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 's+t=%sg*0-f6-y#5oogs(l-m9msf!(#2+p7g=)5(32wj$(2ec%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'codatimetric.urls'

import os

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "%s/templates" % os.getcwd(),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'codatimetric.mapping',
    'codatimetric.search',
)

def get_settings(keylist, t):
    if t == str:
        get = config.get
    elif t == bool:
        get = config.getboolean
    for settings_var in keylist:
        cfg_key = settings_var.replace('_', '-').lower()
        if config.has_option('codatimetric', cfg_key):
            globals()[settings_var] = get('codatimetric', cfg_key)

config = ConfigParser()
if config.read([os.path.join(PROJECT_ROOT, 'codatimetric.cfg')]):
    get_settings(OVERRIDABLE_STRINGS, str)
    get_settings(OVERRIDABLE_BOOLEANS, bool)
