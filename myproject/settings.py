"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

# Loading ENV
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ['*'] 


# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'django_cleanup',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'ckeditor',
    'social_django',

    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'notification',
    'chat',
    'channels',
    'friend',
    'videocall',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Social Django Templates
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

    # Social Django Backends
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'socialNet',
#         'USER': 'postgres',
#         'PASSWORD': os.getenv("PGDB_PWD"),
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATUC_ROOT = os.path.join(BASE_DIR, '../static')
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/home'
# ACCOUNT_LOGOUT_REDIRECT_URL = 'account_logout'
LOGIN_URL = 'login'

CKEDITOR_CONFIGS = {
    'default': {
        'width':'auto',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')     # environment variable containing username
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # environment variable containing password

GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv("GOOGLE_RECAPTCHA_SECRET_KEY")

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

ASGI_APPLICATION = "myproject.routing.application"

CHANNEL_LAYERS = {
    "default":{
        "BACKEND":"channels.layers.InMemoryChannelLayer"
    },
}

SITE_ID = 2     # considering 2nd site in 'Sites' to be 127.0.0.1 (for dev)


STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Social Django

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '55507575741-e8d5dp0vi7l0nf4of2pogcs463k8krib.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_INSTAGRAM_KEY = ''
SOCIAL_AUTH_INSTAGRAM_SECRET = ''

SOCIAL_AUTH_GITHUB_KEY = '5003e1b7bfc57645231a'
SOCIAL_AUTH_GITHUB_SECRET = '61f8ae648a85f59ef0732e9600597f9e687a8049'


SOCIAL_AUTH_FACEBOOK_KEY = '504293705117889'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'cd36c7e28bf4c39ae8c8bbb13f0cbe2e'
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'
