from .base import *
import os
import raven

DEBUG = False

ALLOWED_HOSTS = ['comunidadbiblicadefe.herokuapp.com','comunidadbiblicadefe.org', 'www.comunidadbiblicadefe.org', 'production.comunidadbiblicadefe.org']

# HTTPS CONFIG

#SECURE_SSL_REDIRECT = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HSTS CONFIG

#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_SECONDS = 31536000

# COOKIE SECURE CONFIG

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_CONTENT_TYPE_NOSNIFF = True

INSTALLED_APPS += (
    'storages',
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': os.environ.get('SENTRY_DSN'),
    # If you are using git, you can also automatically configure the
    # release based on the git info.

}

# DATABASE CONFIG

DATABASES = dict(default=dj_database_url.config(default=os.environ.get('DATABASE_URL')))

# S3 AWS CONFIG

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

# GOOGLE ANALYTICS CONFIG

GOOGLE_ANALYTICS_PROPERTY_ID = os.environ.get('GOOGLE_ANALYTICS_ID')
GOOGLE_ANALYTICS_SITE_SPEED = True
