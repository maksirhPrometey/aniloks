from urllib.parse import urlparse

from decouple import config

from .base import *  # noqa: F403

DEBUG = False

_allowed_hosts = list(ALLOWED_HOSTS)  # noqa: F405
for _internal in ("127.0.0.1", "localhost", "web"):
    if _internal not in _allowed_hosts:
        _allowed_hosts.append(_internal)
ALLOWED_HOSTS = _allowed_hosts


def _database_from_url(url: str) -> dict:
    parsed = urlparse(url)
    return {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": parsed.path.lstrip("/"),
        "USER": parsed.username or "",
        "PASSWORD": parsed.password or "",
        "HOST": parsed.hostname or "",
        "PORT": str(parsed.port or 5432),
    }


_database_url = config("DATABASE_URL", default="")
if _database_url:
    DATABASES = {"default": _database_from_url(_database_url)}  # noqa: F811

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_SAMESITE = "Strict"

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    default="",
    cast=lambda v: [s.strip() for s in v.split(",") if s.strip()],
)

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

MIDDLEWARE = [
    m for m in MIDDLEWARE  # noqa: F405
    if m != "whitenoise.middleware.WhiteNoiseMiddleware"
]
