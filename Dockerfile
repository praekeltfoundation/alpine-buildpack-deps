FROM jamiehewland/alpine-buildpack-deps

RUN apk add --no-cache \
        postgresql-dev \
        mariadb-dev
