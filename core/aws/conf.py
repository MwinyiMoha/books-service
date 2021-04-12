import os

from decouple import config


ACCESS_KEY_ID = config("ACCESS_KEY_ID")
SECRET_ACCESS_KEY = config("SECRET_ACCESS_KEY")
STORAGE_BUCKET_NAME = config("BUCKET_NAME")

S3_REGION_NAME = "us-east-2"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=604800"}

AWS_STATIC_URL = AWS_S3_CUSTOM_DOMAIN + "static/"
AWS_MEDIA_URL = AWS_S3_CUSTOM_DOMAIN + "media/"
ADMIN_MEDIA_PREFIX = AWS_STATIC_URL + "admin/"
MEDIA_ROOT = AWS_MEDIA_URL

AWS_FILE_STORAGE = "core.aws.utils.MediaRootS3BotoStorage"
AWS_STATICFILES_STORAGE = "core.aws.utils.StaticRootS3BotoStorage"
DEFAULT_ACL = None
