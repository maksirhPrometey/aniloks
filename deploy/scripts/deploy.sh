#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

COMPOSE_FILES=(-f docker-compose.yml -f docker-compose.prod.yml)

if [[ -f deploy/nginx/docker.prod.conf ]] && [[ -d /etc/letsencrypt/live ]]; then
  COMPOSE_FILES+=(-f docker-compose.ssl.yml)
  echo "==> SSL config detected — HTTPS mode"
else
  echo "==> HTTP-only mode (run setup-ssl.sh after DNS + certbot)"
fi

COMPOSE=(docker compose "${COMPOSE_FILES[@]}")

if [[ ! -f .env ]]; then
  echo "ERROR: .env not found. Copy .env.example and fill in production values."
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "ERROR: Docker not installed."
  echo "Run: sudo bash deploy/scripts/setup-droplet.sh"
  exit 1
fi

free_host_ports() {
  if systemctl is-active --quiet nginx 2>/dev/null; then
    echo "==> Stopping host nginx (conflicts with Docker on :80/:443)..."
    systemctl stop nginx
    systemctl disable nginx 2>/dev/null || true
  fi
  if command -v fuser >/dev/null 2>&1; then
    fuser -k 80/tcp 2>/dev/null || true
    fuser -k 443/tcp 2>/dev/null || true
  fi
}

free_host_ports

echo "==> Building and starting production stack..."
"${COMPOSE[@]}" up -d --build

echo "==> Waiting for web healthcheck..."
for i in $(seq 1 30); do
  if "${COMPOSE[@]}" ps web 2>/dev/null | grep -q "(healthy)"; then
    echo "==> Web is healthy"
    break
  fi
  if [[ "${i}" -eq 30 ]]; then
    echo "WARN: Web healthcheck timeout — check logs:"
    "${COMPOSE[@]}" logs --tail=50 web
    exit 1
  fi
  sleep 3
done

echo "==> Service status:"
"${COMPOSE[@]}" ps

if [[ -f deploy/nginx/docker.prod.conf ]]; then
  echo "==> Verify: curl -sfk https://127.0.0.1/healthz/"
else
  echo "==> Verify: curl -sf http://127.0.0.1/healthz/"
fi

echo ""
echo "==> Deploy OK"
echo ""
echo "    Content seed (після оновлення контенту або першого деплою):"
echo "    docker compose exec web python manage.py migrate"
echo "    docker compose exec web python manage.py seed_from_tz"
echo "    docker compose exec web python manage.py seed_media --force"
echo ""
echo "    docker compose exec web python manage.py createsuperuser"
