# hadolint ignore=DL3007
FROM python:slim

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        alsa-utils \
        curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./app /app

# hadolint ignore=DL3013
RUN pip install --no-cache-dir starlette uvicorn jinja2

EXPOSE 80

# Add health check: curl localhost and expect HTTP 200
HEALTHCHECK --interval=300s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:80/ || exit 1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
