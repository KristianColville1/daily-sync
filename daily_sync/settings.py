"""
Django settings for daily_sync project.

Generated by 'django-admin startproject' using Django 3.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path
import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

development = os.environ.get("DEVELOPMENT", False)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = development

X_FRAME_OPTIONS = "SAMEORIGIN"

ALLOWED_HOSTS = ["daily-sync123.herokuapp.com", "localhost"]

# Application definition

INSTALLED_APPS = [
    "channels",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "django_summernote",
    "crispy_forms",
    "password_validation",
    "home",
    "feed",
    "posts",
    "profiles",
    "chats",
    "search_bar",
]

ASGI_APPLICATION = 'daily_sync.asgi.application'

SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION = "username_email"
ACCOUNT_USERNAME_MIN_LENGTH = 5

LOGIN_REDIRECT_URL = "/feed/"
LOGOUT_REDIRECT_URL = "/"

CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "daily_sync.urls"

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "daily_sync.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if development:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = BASE_DIR / 'emails_sent/'
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("MAILGUN_SMTP_SERVER")
    EMAIL_PORT = os.environ.get("MAILGUN_SMTP_PORT")
    EMAIL_HOST_USER = os.environ.get("MAILGUN_SMTP_LOGIN")
    EMAIL_HOST_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD")
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = "daily.sync@example.com"

DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_PATH = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f'{AUTH_PASSWORD_PATH}.UserAttributeSimilarityValidator',
    },
    {
        'NAME': f'{AUTH_PASSWORD_PATH}.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': f'{AUTH_PASSWORD_PATH}.CommonPasswordValidator',
    },
    {
        'NAME': f'{AUTH_PASSWORD_PATH}.NumericPasswordValidator',
    },
    {
        "NAME": "password_validation.validators.NumValidator",
    },
    {
        "NAME": "password_validation.validators.SymbolValidator",
    },
    {
        "NAME": "password_validation.validators.UppercaseValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

cloudinary.config(cloud_name=os.environ.get("CLOUD_NAME"),
                  api_key=os.environ.get("CLOUDINARY_API_KEY"),
                  api_secret=os.environ.get("CLOUDINARY_API_SECRET"))

STATIC_URL = "/static/"
CLOUD_STORAGE = 'StaticHashedCloudinaryStorage'

STATICFILES_STORAGE = f"cloudinary_storage.storage.{CLOUD_STORAGE}"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
