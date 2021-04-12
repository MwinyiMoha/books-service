from decouple import config

env = config("BOOKS_ENV", None)

if env:
    if env == "PRODUCTION":
        from .production import *
    else:
        from .staging import *
else:
    from .local_settings import *
