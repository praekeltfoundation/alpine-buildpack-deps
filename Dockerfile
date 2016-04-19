FROM jamiehewland/alpine-buildpack-deps:scm

RUN apk add --no-cache --virtual .buildpack-deps \
  autoconf \
  automake \
  bzip2 \
  bzip2-dev \
  curl-dev \
  file \
  g++ \
  gcc \
  geoip-dev \
  glib-dev \
  imagemagick \
  jpeg-dev \
  libc-dev \
  libevent-dev \
  libffi-dev \
  libpng-dev \
  libpq \
  libtool \
  libwebp-dev \
  libxml2-dev \
  libxslt-dev \
  make \
  mysql-client \
  ncurses-dev \
  openssl-dev \
  patch \
  readline-dev \
  sqlite-dev \
  xz-dev \
  yaml-dev \
  zlib-dev
