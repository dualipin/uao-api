#!/bin/sh

CERT_PATH="/etc/letsencrypt/live/uao-api.eastus2.cloudapp.azure.com/fullchain.pem"

if [ -f "$CERT_PATH" ]; then
  echo "✅ Certificado encontrado, iniciando HTTPS"
  cp /nginx-https.conf /etc/nginx/nginx.conf
else
  echo "⚠️ No hay certificado, usando HTTP temporal"
  cp /nginx-http.conf /etc/nginx/nginx.conf
fi

nginx -g 'daemon off;'
