"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.11.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, dj_database_url

import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '__d%ysb=p9yjd2(zkn!fzlk95)swp&=lp!lr-ws+cqqxqx$6uk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sketchyactivity', 
    'compressor',
    'cssmin',
    'jsmin',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'sketchyactivity.context_processors.s3context'
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'd10dclbdpcriqg',
#         'USER': 'gzpgbkerdqzzzm',
#         'PASSWORD': '4aab4367879fc84288d2338c18fc5e441628053eb9f664786aa9e8426866cc47',
#         'HOST': 'ec2-184-73-249-9.compute-1.amazonaws.com',
#     }
# }

# To use remote Heroku db

DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# BEGIN OLD WEBFACTION CONFIG
# STATIC_URL = '/static/'
# STATIC_ROOT = '/home/huntajoseph/webapps/sketchyactivity_static'
#STATICFILES_DIRS = [
#os.path.join(BASE_DIR, 'sketchyactivity/static'),
#]
# END OLD WEBFACTION CONFIG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = 'sketchyactivity' # hashed output to main/static/main folder instead of main/static/CACHE
COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]

USE_S3 = os.getenv('USE_S3') == 'TRUE'
if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_REGION_NAME = 'us-east-2'
    AWS_S3_SIGNATURE_VERSION = 's3v4'

    #PUBLIC_MEDIA_LOCATION = 'media'
    #PUBLIC_MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    #MEDIA_ROOT = MEDIA_URL
    # Private S3 settings
    PRIVATE_MEDIA_LOCATION = 'media'
    PRIVATE_MEDIA_STORAGE = 'sketchyactivity.storage_backends.PrivateMediaStorage'

django_heroku.settings(locals())


def get_cache():
  import os
  try:
    servers = os.environ['MEMCACHIER_SERVERS']
    username = os.environ['MEMCACHIER_USERNAME']
    password = os.environ['MEMCACHIER_PASSWORD']
    return {
      'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': 302400,
        'LOCATION': servers,
        'OPTIONS': {
          'binary': True,
          'username': username,
          'password': password,
          'behaviors': {
            # Enable faster IO
            'no_block': True,
            'tcp_nodelay': True,
            # Keep connection alive
            'tcp_keepalive': True,
            # Timeout settings
            'connect_timeout': 2000, # ms
            'send_timeout': 750 * 1000, # us
            'receive_timeout': 750 * 1000, # us
            '_poll_timeout': 2000, # ms
            # Better failover
            'ketama': True,
            'remove_failed': 1,
            'retry_timeout': 2,
            'dead_timeout': 30,
          }
        }
      }
    }
  except:
    return {
      'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
      }
    }

CACHES = get_cache()
