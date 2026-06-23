from .production import *  # noqa: F403

# TLS завершується в nginx; Gunicorn лише HTTP (healthcheck без 301).
SECURE_SSL_REDIRECT = False
