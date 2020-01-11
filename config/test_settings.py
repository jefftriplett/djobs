import logging

from .settings import *  # noqa


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


logging.disable(logging.CRITICAL)

DEBUG = False

MIGRATION_MODULES = DisableMigrations()

# User a faster password hasher
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

WHITENOISE_AUTOREFRESH = True

# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

MIDDLEWARE = [
    middleware
    for middleware in MIDDLEWARE
    if middleware != "whitenoise.middleware.WhiteNoiseMiddleware"
]
