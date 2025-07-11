# ABOUT

Straight forward IaC setup for the audiophile.

## Content

- Docker compose stack to easily deploy
- Configuration examples for a debian setup
- Dockerfiles to build new or improved images
- Automated CI Pipeline to keep the images up-to-date

## Recommended

- Use watchtower docker container to automate continuous deployment (CD)
- Use a reverse proxy (caddy-docker-proxy)
- Use authelia to protect public facing endpoints

## The stack is

### UI : [mympd](https://jcorporation.github.io/myMPD/010-installation/docker/#volumes)

The user controls the playback in the browser.

### Player : mpd -> FIFO pipe -> Snapcast-server

- All these components are running on the same host.
- MPD will stream the audio to a FIFO pipe.
- Snapcast server will read the FIFO pipe stream and stream it to it's clients.

### Audio-Playback : Snapcast-clients

- A user can playback from any device from Snapcast web client (exposed by snapserver).
- Preferably, playback from snapcast client. This project inclused configurations for:
  - The same server running a client and playing directly through alsa
  - A desktop system running a client and playing through pipewire (not monopolizing the audio ressource, so the audio card can still be used to play from other sources by the logged in user)

### Music library management : Beets

The project includes a version of beets music library manager's docker container that is packed with :

- Ttyd : access the container from the browser and run scripts
- Ranger : Easy and efficient terminal based filebrowser.

## Development

- Linting is done with pre-commit. For this to work, you need an environment with docker (for hadolint and dclint).

## Roadmap

- Automate smoke tests in GHA.
