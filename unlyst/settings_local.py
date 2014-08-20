# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

'''
SET YOUR DB PROPERLY
'''
import os
import sys
import django


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
location = lambda x: os.path.join(BASE_DIR, x)

'''
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'unlyst',
        'USER': 'vagrant',
        #'PASSWORD': 'password',
        #'HOST': '127.0.0.1',
        #'PORT': '5432',
    }
}
'''

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = location('tmp/emails')

SOUTH_TESTS_MIGRATE = False
