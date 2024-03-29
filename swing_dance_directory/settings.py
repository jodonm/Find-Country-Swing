from pathlib import Path
import environ
import os
import gunicorn
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize Django-environ
#env = environ.Env(
    # set casting, default value
   # DEBUG=(bool, False)
#)

# Reading .env file
#environ.Env.read_env(env_file=str(BASE_DIR / '.env'))

#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#load_dotenv(dotenv_path)

dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"

#SECRET_KEY = env('SECRET_KEY')
#DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['find-country-swing.com','find-country-swing.up.railway.app','find-country-swing-2-production.up.railway.app','.localhost', '127.0.0.1', '[::1]']

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
        # Correct the path for the SQLite URL to use BASE_DIR
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'default_db_name'),  # Use Railway's provided variable or a default
        'USER': os.environ.get('POSTGRES_USER', 'default_user'),  # Use Railway's provided variable or a default
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'default_password'),  # Use Railway's provided variable or a default
        'HOST': os.environ.get('PGHOST', 'localhost'),  # Use Railway's provided variable or a default
        'PORT': os.environ.get('PGPORT', '5432'),  # Use Railway's provided variable or a default
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', BASE_DIR / 'dancing_places' / 'templates' / 'dancing_places'],
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

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dancing_places',
    'swing_dance_directory',
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

ROOT_URLCONF = 'swing_dance_directory.urls'

STATIC_URL = 'static/'

import dj_database_url

if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )


STATIC_ROOT = BASE_DIR / 'static/'


WSGI_APPLICATION = 'swing_dance_directory.wsgi.application'


STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_DOMAIN = '.find-country-swing.com'

CSRF_TRUSTED_ORIGINS = [
    'https://find-country-swing.com',
    'http://find-country-swing.com'
]



#use this terminal command for debugging: gunicorn swing_dance_directory.wsgi:application --log-level debug