"""
Django settings for hrlab project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import datetime
import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%uj&%q1_qr&xzb&%4qrv*6_g50e#l8k=z$njfdt@w#gzmcfjlx'

# SECURITY WARNING: don't run with debug turned on in production!
LOCAL = "local"
STAGE = "stage"
BACKEND_ENV = os.environ.get("BACKEND_ENV", LOCAL)
IS_FORM_DATE_CHECK = False

# SECURITY WARNING: don't run with debug turned on in production!
if BACKEND_ENV in (LOCAL, STAGE):
    DEBUG = True
else:
    DEBUG = False

# estimated domain name
# ALLOWED_HOSTS = ['*']
# CSRF_TRUSTED_ORIGINS = ['https://hr-lab.hse.ru']
# CORS_ALLOW_ALL_ORIGINS = True

if BACKEND_ENV == LOCAL:
    ROOT_TO_TEMPLATES = 'backend/coreapi/templates/'
else:
    ROOT_TO_TEMPLATES = '/usr/src/hrlab/templates/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "drf_spectacular",
    "rest_framework",
    "corsheaders",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'hrlab',
    'hrlab.user',
    'hrlab.application',
    'hrlab.project',
    'hrlab.jobopen',
    'hrlab.laboratory',
    'hrlab.manager'

]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.AllowAllUsersModelBackend",)
AUTH_USER_MODEL = "user.User"

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(hours=2),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=2),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=2),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hrlab.urls'

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "hrlab.api.utils.exception_handler",
    "NON_FIELD_ERRORS_KEY": "non_field_error",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    "SEARCH_PARAM": "q",
    "DATETIME_FORMAT": "%s",
    "PAGE_SIZE": 2000,
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS":
        "contrib.drf.pagination.LimitedPageNumberPagination",
}

#TODO add email host
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

if BACKEND_ENV in (LOCAL, STAGE):
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    MEDIA_URL = "/local_media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "local_media")

if BACKEND_ENV in (LOCAL, STAGE):
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] = [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]

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
            ],
        },
    },
]

WSGI_APPLICATION = 'hrlab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if BACKEND_ENV in (LOCAL,):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / './hrlab_db',
        },
    }
else:
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ.get("DATABASE_URL")),
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_CODE_TTL = datetime.timedelta(hours=1)