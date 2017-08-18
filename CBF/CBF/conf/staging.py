from .base import *

DEBUG = True

ALLOWED_HOSTS = ['comunidadbiblicadefe-staging.herokuapp.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATED_EMAIL_BACKEND =  'templated_email.backends.vanilla_django'
