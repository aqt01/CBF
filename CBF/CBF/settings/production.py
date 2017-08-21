from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['comunidadbiblicadefe.herokuapp.com','comunidadbiblicadefe.org', 'www.comunidadbiblicadefe.org',
        'production.comunidadbiblicadefe.org']


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'

INSTALLED_APPS += (
    'storages',
)

DATABASES = dict(default=dj_database_url.config(default=os.environ.get('DATABASE_URL')))

# S3 AWS SETTINGS
AWS_STORAGE_BUCKET_NAME = 'comunidadbf'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_SECRET_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'CBF.custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'CBF.custom_storages.MediaStorage'

# ANYMAIL PRODUCTION CONFIG
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('MAILGUN_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ANYMAIL = {
    'MAILGUN_API_KEY': os.environ.get('MAILGUN_ACTIVATE_KEY'),
    'MAILGUN_SENDER_DOMAIN': os.environ.get('MAILGUN_SENDER_DOMAIN'),
}

ANYMAIL_MAILGUN_API_KEY = os.environ.get('MAILGUN_ACTIVATE_KEY')
