from settings.base import *

from .base.util import get_env_variable

SITE_ID = 1
# local mail config

DEBUG = True

## avoid SMTP madness during development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# INSTALLED_APPS += ('debug_toolbar', )
# INTERNAL_IPS = ('127.0.0.1',)
# MIDDLEWARE_CLASSES += \
# ('debug_toolbar.middleware.DebugToolbarMiddleware', )
# 

STRACKS_URL = get_env_variable('STRACKS_URL', '')

STRACKS_CONNECTOR = None

if STRACKS_URL:
    from stracks_api.connector import HTTPConnector
    STRACKS_CONNECTOR = HTTPConnector(STRACKS_URL)
    MIDDLEWARE_CLASSES += (
        'stracks_api.middleware.StracksMiddleware',
    )
