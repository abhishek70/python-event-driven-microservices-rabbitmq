#!/usr/bin/env bash

# Increasing default HTTP Timeout from 60 to 300
export COMPOSE_HTTP_TIMEOUT=300

# Start all services in background with -d flag
docker-compose up -d