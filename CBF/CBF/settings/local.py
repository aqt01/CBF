from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

CELERY_BROKER_URL = 'amqp://CBF:CristoCentro@localhost:5672/CBF'
CELERY_RESULT_BACKEND = 'amqp://CBF:CristoCentro@localhost:5672/CBF'

SECRET_KEY = 'development'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'

PAYPAL_TEST = True

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
)
