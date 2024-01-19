#!/bin/bash

while [ $# -gt 0 ] ; do
  case $1 in
    -t | --target) W="$2" ;;
  esac
  shift
done

case $W in
    fastapi) poetry run gunicorn -b 0.0.0.0:8000 src.main:app --reload;;
esac
