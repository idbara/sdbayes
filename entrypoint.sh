#!/bin/sh

if [ "$POSTGRES_DB" = "sdbayes-postgres" ]
then
#    echo "Waiting for postgres..."
#
#    while ! nc -z $POSTGRES_URL 5432; do
#      sleep 0.1
#    done

    echo "PostgreSQL started"
fi


exec "$@"
