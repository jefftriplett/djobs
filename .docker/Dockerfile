FROM python:3.7-stretch

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /src/

RUN set -ex && \
    pip install --no-cache-dir \
        -r /src/requirements.txt && \
    rm -rf /root/.cache

COPY . /src/

WORKDIR /src/

ENTRYPOINT ["/src/docker-entrypoint.sh", "--"]
