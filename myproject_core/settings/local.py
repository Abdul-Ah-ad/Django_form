"""
Sample local.py for development overrides.
Rename to local.py and update as needed.
"""



DEBUG = True

SECRET_KEY = 'your-local-dev-secret-key'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'abdulahaddb',         # <-- Use your actual DB name
        'USER': 'abdulahad01',             # <-- Use the built-in superuser
        'PASSWORD': 'ahad',    # <-- Set this password in next step
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Optional for API testing
CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']
