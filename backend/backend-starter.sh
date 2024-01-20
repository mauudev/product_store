#!/bin/bash

while [ $# -gt 0 ] ; do
  case $1 in
    -t | --target) W="$2" ;;
  esac
  shift
done

case $W in
    migrate)
        echo "Waiting for database to be ready..."
        timeout 30 bash -c 'until poetry run alembic -c alembic.ini upgrade head; do sleep 1; done'
        echo "Migration completed"
        ;;
    fastapi) 
        poetry run python src/api/main.py;;
esac
