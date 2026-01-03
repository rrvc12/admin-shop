#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Check if database is running..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done

    echo "The database is up and running!"
fi

#python manage.py flush --no-input
#python manage.py migrate

exec "$@"
