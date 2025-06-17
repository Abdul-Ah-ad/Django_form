from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all hosts during development
ALLOWED_HOSTS = ["*"]

# Database configuration (SQLite for local dev)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', #over riding
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Static and media settings for development
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Optional: Email backend for dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Secret key for local dev only (don't use in production)
SECRET_KEY = 'your-local-secret-key-for-dev-only'

# Optional: CORS and CSRF settings for APIs during local dev
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']
