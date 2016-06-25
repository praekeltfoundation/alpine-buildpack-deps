FROM jamiehewland/alpine-buildpack-deps:slim

RUN apk add --no-cache \
        postgresql-dev \
        mariadb-dev
