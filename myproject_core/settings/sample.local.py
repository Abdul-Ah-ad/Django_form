"""
Sample local.py for development overrides.
Rename to local.py and update as needed.
"""

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev_db.sqlite3',
    }
}

SECRET_KEY = 'your-local-dev-secret-key'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
