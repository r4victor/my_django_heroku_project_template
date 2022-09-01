#!/bin/sh

psql -U postgres -c "create database ${POSTGRES_DB}"
psql -U postgres -c "create user ${POSTGRES_USER}"
psql -U postgres -c "alter role ${POSTGRES_USER} with password '${POSTGRES_PASSWORD}'"
psql -U postgres -c "grant all privileges on database ${POSTGRES_DB} to ${POSTGRES_USER}"
psql -U postgres -c "alter database ${POSTGRES_DB} owner to ${POSTGRES_USER}"
