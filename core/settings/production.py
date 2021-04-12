import dj_database_url

from .base import *
from core.aws.conf import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = "/static/"
MEDIA_URL = "/media/"
STATIC_ROOT = AWS_STATIC_URL
MEDIA_ROOT = AWS_MEDIA_URL

DEFAULT_FILE_STORAGE = AWS_FILE_STORAGE
STATICFILES_STORAGE = AWS_STATICFILES_STORAGE
AWS_ACCESS_KEY_ID = ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = STORAGE_BUCKET_NAME
AWS_S3_REGION_NAME = S3_REGION_NAME
AWS_DEFAULT_ACL = DEFAULT_ACL
