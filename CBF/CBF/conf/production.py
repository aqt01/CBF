from .base import *

DEBUG = False

ALLOWED_HOSTS = ['comunidadbiblicadefe.herokuapp.com']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

TEMPLATED_EMAIL_BACKEND =  'templated_email.backends.vanilla_django'
