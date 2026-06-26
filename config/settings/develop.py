from decouple import config
from .base import *  # noqa

SECRET_KEY = config("SECRET_KEY", default="dev-only-insecure-key-do-not-use-in-prod")

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

WHITENOISE_AUTOREFRESH = True

if not config("RESEND_API_KEY", default=""):
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CONTENT_SECURITY_POLICY = {
    "EXCLUDE_URL_PREFIXES": ("/admin/",),
    "DIRECTIVES": {
        "default-src": ["'self'"],
        "script-src": ["'self'", "'unsafe-inline'"],
        "style-src": ["'self'", "https://fonts.googleapis.com", "'unsafe-inline'"],
        "font-src": ["'self'", "https://fonts.gstatic.com"],
        "img-src": ["'self'", "data:"],
        "connect-src": ["'self'", "http://127.0.0.1:7438"],
        "frame-ancestors": ["'none'"],
        "media-src": ["'self'"],
    }
}
