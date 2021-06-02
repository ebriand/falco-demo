#!/usr/bin/env sh

apt-get update
apt-get install -y docker.io 
apt-get install -y docker-compose

mkdir -p /app
cat <<EOF > /app/docker-compose.yaml
version: "3.1"
services:
  falcosidekick:
    image: falcosecurity/falcosidekick
    environment:
     - WEBUI_URL=http://ui:2802
    ports:
     - 2801:2801
  ui:
    image: falcosecurity/falcosidekick-ui
    ports:
     - 80:2802
EOF

cd /app || exit
docker-compose up -d
