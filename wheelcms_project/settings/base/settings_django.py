SITE_ID = 1

# Make this unique, and don't share it with anybody. Set to none so django
# will complain

from .util import get_env_variable

SECRET_KEY = get_env_variable('SECRET_KEY', None)
if SECRET_KEY is None:
    from logging import warning
    warning("$SECRET_KEY not set, using fixed SECRET_KEY in stead. DO NOT USE THIS IN PRODUCTION SITES!")
    SECRET_KEY="not-random-do-not-use-this-key-in-production"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    "wheelcms_axle.context_processors.configuration",
    "wheelcms_axle.context_processors.toolbar",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',

    'django.contrib.sitemaps',

    'south',
    'haystack',

    'wheelcms_project',
    'wheelcms_theme_bootswatch',
    'wheelcms_axle',
    'wheelcms_spokes',
    'wheelcms_categories',
    'wheelcms_simplecontact',

    'taggit',
    'tinymce',
    'two.ol',
    'two.bootstrap',
    'twotest',

    'userena',
    'guardian'


)


TESTING = False  ## assume we're not running a unit test, override explicitly
