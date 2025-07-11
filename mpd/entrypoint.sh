#!/bin/sh
set -eux

TARGET="/var/lib/mpd"   # Changed to match Dockerfile

if [ -z "$(ls -A "$TARGET" 2>/dev/null || true)" ]; then
    touch "$TARGET/state"
else
    echo "[init] $TARGET already populated, skipping."
fi
chown -R 1000:1000 $TARGET /pipe

exec su-exec 1000:1000 /usr/bin/mpd --no-daemon --stdout /etc/mpd.conf
