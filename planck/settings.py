"""
Django settings for planck project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from confo.Confo import Confo
import confo.Backends as BE

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR/"configs"
config = Confo()
ENV = "DEVELOPMENT"
if ENV != "PROD":
    """
    Setup a file backend for all non prod configurations, 
    The different non prod environments can be controlled by namespacing
    """
    cred = {"config_path":str(CONFIG_DIR)}
    config.load_backend(credentials=cred,name="planck_non_prod_backends",backend_type=BE.FILE_BACKEND)
    config.activate_backend("planck_non_prod_backends")

    if ENV == "DEVELOPMENT":
        config.use_namespace("development_env")
    else:
        config.use_namespace("local_compose_env")

    DEBUG = True
elif ENV == "PROD":
    """
    Setup a more production appropriate backend backend for production deployments:
    1. Zookeeper
    2. ETCD
    3. VAULT
    """
    DEBUG = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-px#fh6+q13yst^_7u)5gcv0^r0bd^iig(#6weseku64l=k1moa'

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = []


# Application definition
LOCAL_APPS = [
 'ProjectManager',
 'VersionControlManager',
 'Utilities'
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions'
]
INSTALLED_APPS += LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'planck.urls'

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

WSGI_APPLICATION = 'planck.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DB=config.get("database")
DATABASES = {
    'default': {
        'ENGINE': DB.get("ENGINE"),
        'NAME': DB.get('DB_NAME'),
        'USER': DB.get('DB_USER'),
        'PASSWORD': DB.get('DB_PASSWORD'),
        'HOST': DB.get('DB_HOST'),
        'PORT': DB.get('DB_PORT'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
