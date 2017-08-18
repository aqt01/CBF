from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['comunidadbiblicadefe.herokuapp.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django'

INSTALLED_APPS += (
    'storages',
)

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# S3 AWS SETTINGS
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
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
