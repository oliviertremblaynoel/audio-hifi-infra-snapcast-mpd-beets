######################
# 1. Build the webapp
FROM node:18-alpine AS builder

# hadolint ignore=DL3018
RUN apk add --no-cache git

WORKDIR /app

RUN git clone https://github.com/badaix/snapweb . \
    && npm ci \
    && npm run build

######################
# 2. Build final image
# hadolint ignore=DL3007
FROM alpine:latest

COPY --from=builder /app/dist /snapweb
COPY snapserver.conf /etc/snapserver.conf.new

LABEL \
    org.opencontainers.image.title="Snapcast client" \
    org.opencontainers.image.description="Snapcast - Synchronous audio player - Server" \
    org.opencontainers.image.version="1.0" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.authors="Olivier Tremblay-Noel" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/oliviertremblaynoel/snapcast-server" \
    org.opencontainers.image.source="https://github.com/oliviertremblaynoel/audiophile-setup"

# hadolint ignore=DL3018
RUN apk add --no-cache \
    snapcast-server \
    ; \
    mkdir /root/.config/snapserver ; \
    touch /root/.config/snapserver/server.json \
    ; \
    cp /etc/snapserver.conf /etc/snapserver.conf.backup ; \
    mv /etc/snapserver.conf.new /etc/snapserver.conf ;

VOLUME /root/.config/snapserver
WORKDIR /root/.config/snapserver

# Audio Stream
EXPOSE 1704
# WEBAPP
EXPOSE 1780

ENTRYPOINT ["snapserver"]

HEALTHCHECK --interval=300s --timeout=5s --start-period=5s --retries=3 \
  CMD nc -z localhost 1704 || exit 1
