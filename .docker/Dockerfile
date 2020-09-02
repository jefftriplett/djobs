# syntax = docker/dockerfile:experimental

FROM segment/chamber:2 AS chamber

FROM python:3.7-stretch AS dev

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /src/

RUN --mount=type=cache,target=/root/.cache/pip pip install -r /tmp/requirements.txt

WORKDIR /src/

FROM dev AS production

COPY --from=chamber /chamber /bin/chamber

COPY . /src/
#
