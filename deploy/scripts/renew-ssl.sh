#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

COMPOSE="docker compose -f docker-compose.yml -f docker-compose.prod.yml -f docker-compose.ssl.yml"

if [[ ! -f deploy/nginx/docker.prod.conf ]]; then
  echo "ERROR: SSL not configured. Run ./deploy/scripts/setup-ssl.sh first."
  exit 1
fi

echo "==> Renewing certificates..."
certbot renew --quiet

echo "==> Reloading nginx..."
${COMPOSE} exec nginx nginx -s reload

echo "==> SSL renewal complete."
