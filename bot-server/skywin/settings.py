"""
Django settings for skywin project on Heroku. Fore more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "zxu_l$p+swpk7sg&(3&*@j0jai&+ov+@okh59x+r5v6tfhquin"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = (

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # local apps
    'bot',

    # third party apps
    'rest_framework',
    'telegrambot',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'skywin.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Guido Meda docet
        'DIRS': ['templates', ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                # Django
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'skywin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# Internationalization and localization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Rome'  # 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = False
LOCALE_PATHS = (BASE_DIR + '/locale', )

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'bot-server/staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_LOG_LEVEL = 'WARNING'

_HANDLERS = {
    'console': {
        'level': DEFAULT_LOG_LEVEL,
        'formatter': 'default',
        'class': 'logging.StreamHandler'
    },
}

LOG_FORMAT = '[%(levelname)s %(asctime)s %(name)s %(module)s: %(processName)s] %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': LOG_FORMAT
        }
    },
    'handlers': _HANDLERS,
    'loggers': {
        'django': {
            'level': DEFAULT_LOG_LEVEL,
        },
        'custom': {
            'level': DEFAULT_LOG_LEVEL,
        },
    },
    'root': {
        'handlers': _HANDLERS.keys(),
        'level': DEFAULT_LOG_LEVEL,
    }
}


######################
# Url configurations #
######################
DOMAIN = "example.com"
DOMAIN_URL = "http://www." + DOMAIN
LOGIN_URL = "/login/"
PRIVACY_POLICY_URL = ""
FACEBOOK_APP_ID = "..."
EMAIL_ADDRESS_FOR_SUPPORT = "support@" + DOMAIN


################
# Telegram Bot #
################
TELEGRAM_BOT_HANDLERS_CONF = "bot.bot_handlers"
TELEGRAM_BOT_TOKEN_EXPIRATION = "2"  # tow hours before a token expires
TELEGRAM_BOT_TOKEN = "232161513:AAEsreQl7mGA-mtPRWHmkXwFT_BRmJNO8bs"


#########################
# Django REST Framework #
#########################
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions, or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# Loading test/prod settings based on ENV settings
ENV = os.environ.get('ENV', 'local')
if ENV == 'prod':
    import dj_database_url
    DEBUG = False
    DATABASES['default'] = dj_database_url.config()
    # Enable Connection Pooling (if desired)
    DATABASES['default']['ENGINE'] = 'django_postgrespool'
    # Allow all host headers
    ALLOWED_HOSTS = ['skywin.herokuapp.com']
