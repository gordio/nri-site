"""
Django settings for nri project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin.apps.AdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pipeline',
    'easy_thumbnails',
    'gallery',
    'contacts',
    'captcha',
)

CAPTCHA_FONT_SIZE = 20
CAPTCHA_LENGTH = 3
CAPTCHA_LETTER_ROTATION = (-15, 15)
CAPTCHA_BACKGROUND_COLOR = '#EFEFEF'
CAPTCHA_FOREGROUND_COLOR = '#111111'
CAPTCHA_TIMEOUT = 10
CAPTCHA_NOISE_FUNCTIONS = ('captcha.helpers.noise_dots', )
CAPTCHA_FILTER_FUNCTIONS = None

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS_COMPRESSOR = 'nri.cssmin.CSSMinCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
          'css/reset.css',
          'css/layout.css',
          'css/messages.css',
          'css/icon-font.css',
        ),
        'output_filename': 'assets/main.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'gallery': {
        'source_filenames': (
          'css/gallery-photos.css',
          'css/image-viewer.css'
        ),
        'output_filename': 'assets/gallery.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    'contacts': {
        'source_filenames': (
          'css/form.css',
          'css/contacts.css'
        ),
        'output_filename': 'assets/contacts.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
}

PIPELINE_DISABLE_WRAPPER = True
PIPELINE_JS = {
    'gallery': {
        'source_filenames': (
          'js/image-viewer.js',
          'js/image-viewer-init.js',
        ),
        'output_filename': 'assets/gallery.js',
    }
}

THUMBNAIL_ALIASES = {
    '': {
        'gallery_thumb': {'size': (210, 210), 'crop': "smart"},
    },
}

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nri.urls'

WSGI_APPLICATION = 'nri.wsgi.application'


TEMPLATE_DIRS = (BASE_DIR + '/templates/', )


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    BASE_DIR + '/locale',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR + '/public/static/'
STATICFILES_DIRS = (BASE_DIR + '/static/', )
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR + '/public/media/'


from nri.settings_local import *
