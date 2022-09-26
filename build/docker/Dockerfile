FROM python:3.9-slim

RUN mkdir -p app/

COPY src/ app/

RUN apt-get update -y -qq && \
    python3 -m pip install -U pip && \
    python3 -m pip install -r app/requirements.txt
