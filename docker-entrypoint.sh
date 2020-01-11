#!/usr/bin/env bash
set -eo pipefail

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
