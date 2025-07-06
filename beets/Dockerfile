# hadolint ignore=DL3007
FROM lscr.io/linuxserver/beets:latest

LABEL \
    org.opencontainers.image.title="Beets TTYD" \
    org.opencontainers.image.description="The Beets container with ttyd" \
    org.opencontainers.image.version="1.0" \
    org.opencontainers.image.licenses="GPL-3.0" \
    org.opencontainers.image.authors="Olivier Tremblay-Noel" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/oliviertremblaynoel/beets" \
    org.opencontainers.image.source="https://github.com/oliviertremblaynoel/audiophile-setup"

# hadolint ignore=DL3018
RUN useradd -u 1000 -g 1000 -m -s /bin/bash beets && \
    apk add --no-cache \
    ttyd \
    bash \
    ranger \
    micro \
    rdfind \
    most \
    nnn \
    mc

EXPOSE 7681 8337

HEALTHCHECK --interval=300s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -fs http://localhost:7681 || exit 1

ENTRYPOINT [ "ttyd", "-u", "1000", "-g", "1000", "-W", "-p", "7681", "-t", "titleFixed=Beets", "bash"]
