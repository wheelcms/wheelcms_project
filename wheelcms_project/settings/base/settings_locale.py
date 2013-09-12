from .util import get_env_variable

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Wheel translation support. This lives in its own set of configuration
# options for now, which may mean some duplocation

LANGUAGES = (('en', 'English'), ('nl', 'Nederlands'))
CONTENT_LANGUAGES = LANGUAGES
FALLBACK = 'en'

## Force the site (content + interface) into a specific language?
FORCE_LANGUAGE = get_env_variable('FORCE_LANGUAGE', None)

## Default language if it cannot be determined otherwise
LANGUAGE_CODE = 'en'

## map languages to domains. If there are different domains per language,
## these are used to construct the correct URL for the language switch
LANGUAGE_DOMAINS = {}
