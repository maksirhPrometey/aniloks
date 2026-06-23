#!/bin/sh
set -e

echo "==> Waiting for PostgreSQL..."
if [ -n "${DATABASE_URL:-}" ]; then
  python <<'PY'
import os
import sys
import time

import psycopg2

url = os.environ.get("DATABASE_URL", "")
if not url:
    sys.exit(0)

for attempt in range(30):
    try:
        psycopg2.connect(url)
        print("==> DB ready")
        break
    except psycopg2.OperationalError:
        time.sleep(2)
else:
    print("FATAL: DB not ready after 60s")
    sys.exit(1)
PY
fi

python manage.py migrate --noinput

if [ "${DJANGO_SETTINGS_MODULE:-}" != "config.settings.develop" ]; then
  python manage.py check --deploy
  python manage.py collectstatic --noinput

  mkdir -p staticfiles media
  touch staticfiles/.keep media/.keep

  _static_count=$(find /app/staticfiles -type f 2>/dev/null | wc -l | tr -d ' ')
  echo "==> static files: ${_static_count}"
  if [ "${_static_count:-0}" -lt 5 ]; then
    echo "WARN: staticfiles count low — check STATIC_ROOT and collectstatic"
  fi
fi

exec "$@"
