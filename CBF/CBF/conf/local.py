from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL',
    'postgres://cbf:cbf@localhost:5432/cbf'))

SECRET_KEY = 'development'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATED_EMAIL_BACKEND =  'templated_email.backends.vanilla_django'

PAYPAL_TEST = True
