#!/usr/bin/env bash
# exit on error
set -o errexit

gunicorn iwaki_autumn.wsgi:application