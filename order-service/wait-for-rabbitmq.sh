#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

while ! nc -z $RABBITMQ_HOST $RABBITMQ_PORT; do
  >&2 echo "RabbitMQ is unavailable - sleeping"
  sleep 1
done

>&2 echo "RabbitMQ started"
exec $cmd