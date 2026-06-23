#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: CERTBOT_EMAIL=you@example.com $0 primary-domain [www-domain ...]"
  echo "Example: CERTBOT_EMAIL=admin@aniloks.com.ua $0 aniloks.com.ua www.aniloks.com.ua"
  exit 1
fi

EMAIL="${CERTBOT_EMAIL:-}"
if [[ -z "${EMAIL}" ]]; then
  echo "ERROR: set CERTBOT_EMAIL environment variable"
  exit 1
fi

PRIMARY_DOMAIN="$1"
shift
EXTRA_DOMAINS=("$@")
ALL_DOMAINS=("${PRIMARY_DOMAIN}" "${EXTRA_DOMAINS[@]}")

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT_DIR}"

COMPOSE_BASE="docker compose -f docker-compose.yml -f docker-compose.prod.yml"
COMPOSE_SSL="${COMPOSE_BASE} -f docker-compose.ssl.yml"
TEMPLATE="${ROOT_DIR}/deploy/nginx/docker.prod.conf.template"
OUTPUT="${ROOT_DIR}/deploy/nginx/docker.prod.conf"
WEBROOT="${ROOT_DIR}/certbot_www"

set_env_var() {
  local key="$1"
  local val="$2"
  if grep -q "^${key}=" .env 2>/dev/null; then
    sed -i "s|^${key}=.*|${key}=${val}|" .env
  else
    echo "${key}=${val}" >> .env
  fi
}

append_allowed_host() {
  local host="$1"
  local current
  current="$(grep '^ALLOWED_HOSTS=' .env | cut -d= -f2- | tr -d ' ' || echo "")"
  if [[ -z "${current}" ]]; then
    set_env_var "ALLOWED_HOSTS" "${host}"
    return
  fi
  if [[ ",${current}," != *",${host},"* ]]; then
    set_env_var "ALLOWED_HOSTS" "${current},${host}"
  fi
}

if [[ ! -f .env ]]; then
  echo "ERROR: .env not found"
  exit 1
fi

echo "==> Primary domain: ${PRIMARY_DOMAIN}"
echo "==> Stopping nginx (certbot standalone needs port 80)..."
${COMPOSE_BASE} stop nginx 2>/dev/null || true

if systemctl is-active --quiet nginx 2>/dev/null; then
  echo "==> Stopping host nginx..."
  systemctl stop nginx
fi

if ! command -v certbot >/dev/null 2>&1; then
  echo "==> Installing certbot..."
  apt-get update
  apt-get install -y certbot
fi

DOMAIN_ARGS=()
for domain in "${ALL_DOMAINS[@]}"; do
  DOMAIN_ARGS+=("-d" "${domain}")
done

echo "==> Requesting certificate: ${ALL_DOMAINS[*]}"
certbot certonly --standalone \
  "${DOMAIN_ARGS[@]}" \
  --agree-tos \
  --non-interactive \
  --email "${EMAIL}"

if [[ ! -f "/etc/letsencrypt/live/${PRIMARY_DOMAIN}/fullchain.pem" ]]; then
  echo "ERROR: certificate not found at /etc/letsencrypt/live/${PRIMARY_DOMAIN}/"
  exit 1
fi

mkdir -p "${WEBROOT}/.well-known/acme-challenge"

echo "==> Generating deploy/nginx/docker.prod.conf..."
sed "s/__PRIMARY_DOMAIN__/${PRIMARY_DOMAIN}/g" "${TEMPLATE}" > "${OUTPUT}"

echo "==> Updating .env..."
set_env_var "DJANGO_SETTINGS_MODULE" "config.settings.docker"
set_env_var "USE_HTTPS" "true"
set_env_var "SITE_URL" "https://${PRIMARY_DOMAIN}"
set_env_var "SECURE_SSL_REDIRECT" "False"
for domain in "${ALL_DOMAINS[@]}"; do
  append_allowed_host "${domain}"
done

ORIGINS=""
for domain in "${ALL_DOMAINS[@]}"; do
  if [[ -n "${ORIGINS}" ]]; then
    ORIGINS="${ORIGINS},"
  fi
  ORIGINS="${ORIGINS}https://${domain}"
done
set_env_var "CSRF_TRUSTED_ORIGINS" "${ORIGINS}"

if command -v ufw >/dev/null 2>&1; then
  ufw allow 443/tcp >/dev/null 2>&1 || true
fi

echo "==> Starting stack with HTTPS..."
${COMPOSE_SSL} up -d --build

echo "==> Verifying nginx config..."
${COMPOSE_SSL} exec nginx nginx -t

echo ""
echo "==> SSL enabled."
echo "    https://${PRIMARY_DOMAIN}/"
echo "    https://${PRIMARY_DOMAIN}/healthz/"
echo ""
echo "Renewal: ./deploy/scripts/renew-ssl.sh"
