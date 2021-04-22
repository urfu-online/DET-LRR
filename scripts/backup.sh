#!/bin/bash

profile="production"

docker-compose -f ${profile}.yml down && \
  docker-compose -f local.yml up -d postgres && \
  docker-compose -f local.yml exec postgres backup
docker cp `docker ps -aqf "name=lrr_postgres"`:/backups . && \
  docker-compose -f local.yml down;
