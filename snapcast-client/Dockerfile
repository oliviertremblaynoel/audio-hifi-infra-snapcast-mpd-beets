# hadolint ignore=DL3007
FROM alpine:latest

LABEL org.opencontainers.image.authors="Olivier Tremblay-Noel" \
    org.opencontainers.image.title="Snapcast client" \
    org.opencontainers.image.description="Snapcast - Synchronous audio player - Client" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.version="1.0" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/oliviertremblaynoel/snapcast-client" \
    org.opencontainers.image.source="https://github.com/oliviertremblaynoel/audiophile-setup"

# hadolint ignore=DL3018
RUN apk add --no-cache \
    snapcast-client \
    pipewire-alsa

COPY ./asound.conf /etc/asound.conf

# hadolint ignore=DL3025
ENTRYPOINT snapclient --host "$SNAP_SERVER_HOSTNAME" --hostID "$CLIENT_ID" --player "$PLAYER_TYPE"

HEALTHCHECK --interval=300s --timeout=5s --retries=3 \
    CMD pgrep snapclient || exit 1
