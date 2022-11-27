#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pwd
ls
cd ./iwaki_autumun
python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py create_db_postgresql
python manage.py create_superuser
