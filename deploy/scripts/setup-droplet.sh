#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root: sudo $0"
  exit 1
fi

echo "==> Installing Docker..."
curl -fsSL https://get.docker.com | sh
usermod -aG docker "${SUDO_USER:-root}" 2>/dev/null || true

echo "==> Installing git, ufw..."
apt-get update
apt-get install -y git ufw

echo "==> Firewall..."
ufw allow OpenSSH
ufw allow 80/tcp
ufw allow 443/tcp
ufw --force enable

APP_DIR="/var/www/nikola"
mkdir -p "${APP_DIR}"

echo ""
echo "==> Droplet ready. Next steps:"
echo "  git clone <repo-url> ${APP_DIR}"
echo "  cd ${APP_DIR} && cp .env.example .env && nano .env"
echo "  chmod +x deploy/scripts/*.sh"
echo "  ./deploy/scripts/deploy.sh"
echo ""
echo "  DNS: A @ → 134.209.119.77"
echo "  DNS: A www → 134.209.119.77"
echo ""
echo "  SSL (після DNS):"
echo "  CERTBOT_EMAIL=admin@aniloks.com.ua ./deploy/scripts/setup-ssl.sh aniloks.com.ua www.aniloks.com.ua"
