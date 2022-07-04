#!/bin/bash

if [ -e /database/db.sqlite3 ]
then
  echo 'Database found.'
else
  echo 'Creating Database.'
  python manage.py migrate
  python manage.py makemigrations
  python manage.py migrate
  export DJANGO_SUPERUSER_PASSWORD="admin"
  python manage.py createsuperuser --username admin --email admin@example.com --noinput
  unset DJANGO_SUPERUSER_PASSWORD
fi

service nginx start
gunicorn smarthome.wsgi:application