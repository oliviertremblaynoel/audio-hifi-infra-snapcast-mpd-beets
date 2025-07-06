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

# hadolint ignore=DL3018
RUN set -eux ; \
    apk --no-cache add \
        mpd \
        mpc \
    ; \
    mkdir /var/lib/mpd/data ; \
    touch /var/lib/mpd/data/database \
        /var/lib/mpd/data/state \
        /var/lib/mpd/data/sticker.sql \
    ; \
    chown -R mpd:audio /var/lib/mpd ; \
    cp /etc/mpd.conf /etc/mpd.conf.backup ; \
    mv /etc/mpd.conf.new /etc/mpd.conf ; \
    chown -R mpd:audio /etc/mpd.con*

VOLUME /var/lib/mpd
WORKDIR /var/lib/mpd
EXPOSE 6600 8000

CMD ["/usr/bin/mpd", "--no-daemon", "--stdout", "/etc/mpd.conf"]

HEALTHCHECK --interval=300s --timeout=5s --retries=3 \
    CMD nc -zvw3 127.0.0.1 6600 || exit 1
