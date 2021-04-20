#!/bin/bash

bck_file="$1"
profile="production"

if [ -z "$bck_file" ]
then
  echo "Wrong backup filename!"
  exit 1
fi

docker-compose -f ${profile}.yml down;
sleep 20
docker-compose -f local.yml up -d postgres;
sleep 20
docker cp ./backups det-lrr_postgres_1:/;
sleep 5
docker-compose -f local.yml exec postgres restore ${bck_file} \
  && docker-compose -f local.yml down;
docker-compose -f ${profile}.yml up -d;
