FROM python:latest

ENV POETRY_VERSION=1.1.13
RUN python3 -m pip install poetry==$POETRY_VERSION

WORKDIR /code