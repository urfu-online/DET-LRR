#!/bin/bash

profile="local"

docker-compose -f local.yml exec postgres backup
docker cp `docker ps -aqf "name=lrr_postgres"`:/backups .
