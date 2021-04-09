#!/bin/sh

set -e

# Wait script
# https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh
if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for MySQL"

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "MySQL started"
fi


echo "Waiting for RabbitMQ"
echo "$RABBITMQ_HOST"
while ! nc -z $RABBITMQ_HOST $RABBITMQ_PORT; do
  sleep 0.1
done

echo "RabbitMQ started"


#python manage.py flush --no-input
python manage.py migrate

exec "$@"