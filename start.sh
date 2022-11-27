#!/usr/bin/env bash
# exit on error
set -o errexit

cd iwaki_autumn
gunicorn iwaki_autumn.wsgi:application