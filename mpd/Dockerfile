# hadolint ignore=DL3007
FROM alpine:latest

LABEL \
    org.opencontainers.image.title="MPD" \
    org.opencontainers.image.description="MPD - Music Player Daemon" \
    org.opencontainers.image.version="1.0" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.authors="Olivier Tremblay-Noel" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/oliviertremblaynoel/beets" \
    org.opencontainers.image.source="https://github.com/oliviertremblaynoel/audiophile-setup"

COPY mpd.conf /etc/mpd.conf.new
COPY entrypoint.sh /entrypoint.sh

# hadolint ignore=DL3018
RUN set -eux; \
    apk --no-cache add mpd mpc su-exec; \
    addgroup -g 1000 mpduser; \
    adduser -D -u 1000 -G mpduser mpduser; \
    mkdir -p \
        /var/lib/mpd \
        /run/mpd \
        /pipe; \
    cp /etc/mpd.conf /etc/mpd.conf.backup; \
    mv /etc/mpd.conf.new /etc/mpd.conf; \
    chmod +x /entrypoint.sh; \
    chown -R 1000:1000 \
        /pipe \
        /var/lib/mpd \
        /etc/mpd.conf* \
        /entrypoint.sh \
        /run/mpd

VOLUME /pipe
VOLUME /var/lib/mpd

EXPOSE 6600 8000
HEALTHCHECK --interval=300s --timeout=5s --retries=3 \
    CMD nc -zvw3 127.0.0.1 6600 || exit 1

ENTRYPOINT ["/entrypoint.sh"]
