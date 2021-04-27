from .base import *

DEBUG = False

ADMINS = (
    ('Biko C', 'bikocodes@gmail.com'),
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa',
    }
}