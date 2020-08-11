FROM segment/chamber:2 AS chamber

FROM python:3.7-stretch AS dev

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /src/

RUN set -ex && \
    pip install --no-cache-dir \
        -r /src/requirements.txt && \
    rm -rf /root/.cache

WORKDIR /src/

FROM dev AS production

COPY --from=chamber /chamber /bin/chamber

COPY . /src/
