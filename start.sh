#!/bin/bash
source .env
# docker run --rm --name postgres-container -e POSTGRES_PASSWORD=${PG_PWD} -d -p 5432:5432 -v ${HOST_FOLDER}:/var/lib/postegresql/data postgres
docker-compose --verbose up -d --build
# docker-compose up -d --build