# Settings for live deployed environments: vagrant, staging, production, etc
from .base import *  # noqa

import dj_database_url

SECRET_KEY = os.environ['SECRET_KEY']


DATABASES['default'] = dj_database_url.config()

INSTALLED_APPS += (
    'storages',
)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

DEBUG = os.environ.get('DEBUG', False)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(';')


MIDDLEWARE += (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# CORS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = os.environ.get('CORS_ORIGIN_WHITELIST', '').split(',')
