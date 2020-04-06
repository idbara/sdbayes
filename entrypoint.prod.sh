#!/bin/sh

if [ "$POSTGRES_DB" = "sdbayes-postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_URL 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$FLASK_CONFIG" = "production" ]
then
  DBNAME="$POSTGRES_DB"
  DBEXISTS=$(PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$POSTGRES_URL" -U "$POSTGRES_USER" \
            -d "$DBNAME" --command "select * from users" > /dev/null; echo "$?")
    if [ $DBEXISTS -eq 0 ];then
        echo "A database with the name $DBNAME already exists."
        python manage.py db stamp head
        python manage.py db migrate
        python manage.py db upgrade
    else
        echo " database $DBNAME does not exist."
        echo "Creating the database tables..."
        python manage.py recreate_db
        python manage.py import_dev
        echo "Tables created"
    fi
fi
exec "$@"
