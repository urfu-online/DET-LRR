#!/bin/bash

source .env

bck_file=""
profile="production.urfu"


for i in "$@"
do
case $i in
    -f=*|--filename=*|filename=*)
      bck_file="${i#*=}"
      shift # past argument=value
    ;;
     -e=*|--environment=*|env=*)
      profile="${i#*=}"
      shift
    ;;
    *)
      echo "Unknown parameter passed: $i"; exit 1
    ;;
esac
done

if [ -z "$bck_file" ]
then
  echo "Wrong backup filename. !"
  exit 1
fi

docker-compose -f "${profile}".yml down;
docker-compose -f local.yml up -d postgres;
docker cp ${WEB_APP_PATH}/backups "$(docker ps -aqf 'name=lrr_postgres')":/;
docker-compose -f local.yml exec postgres restore "${bck_file}" \
  && docker-compose -f local.yml down;
docker-compose -f "${profile}".yml up -d;
