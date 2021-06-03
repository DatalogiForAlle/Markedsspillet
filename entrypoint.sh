#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py flush --no-input
python manage.py migrate

echo "${0}: collecting static files."
python manage.py collectstatic --noinput --clear

# cp -rv static/* static_shared/

echo "${0}: Running development server."
python manage.py runserver 0.0.0.0:8000