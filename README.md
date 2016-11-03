# alpine-buildpack-deps

[![Build Status](https://img.shields.io/travis/praekeltfoundation/alpine-buildpack-deps/develop.svg)](https://travis-ci.org/praekeltfoundation/alpine-buildpack-deps)

An attempt at a "buildpack-deps"-like Docker image with Alpine Linux

### Images
The base image is the [official Docker Alpine image](https://hub.docker.com/_/alpine/).

This repo contains a set of images similar to the official [buildpack-deps](https://hub.docker.com/_/buildpack-deps/) images.

| **Tag**  | **Base image** | **Description**                                               |
|----------|----------------|---------------------------------------------------------------|
| `curl`   | `alpine:3.4`   | Alpine with `curl` and `wget`                                 |
| `scm`    | `:curl`        | `:curl` with source control management (SCM) tools            |
| `slim`   | `:scm`         | `:scm` with build tools and development libraries             |
| `latest` | `:slim`        | `:slim` with database development libraries (see notes below) |

## Caveats
* A best effort was made to find equivalent Alpine packages for the Debian packages in the official buildpack-deps. The packages may not always be *100% equivalent*.
* The code you're compiling in buildpack-deps could make assumptions about the host that are not necessarily true for Alpine Linux. For example:
  * That the standard Unix tools are the GNU implementations
  * That the standard C library is `glibc`
  * That the paths to development files are the Debian paths
* The default/`latest` tag for this image is *not* smaller than the Debian/Ubuntu-based buildpack-deps images, although it is roughly the same size (~190MB compressed, ~660MB uncompressed). The reason for this is that the Alpine development libraries for PostgreSQL and MySQL are significantly bigger than the Debian ones. If you are hoping to make a small "buildpack-deps"-based Docker image, you're probably doing Docker images wrong.

## Packages
The following sources were used to find the required packages:
* [`curl`](https://github.com/docker-library/buildpack-deps/blob/a0a59c61102e8b079d568db69368fb89421f75f2/jessie/curl/Dockerfile)
* [`scm`](https://github.com/docker-library/buildpack-deps/blob/1845b3f918f69b4c97912b0d4d68a5658458e84f/jessie/scm/Dockerfile)
* [`latest`](https://github.com/docker-library/buildpack-deps/blob/e7534be05255522954f50542ebf9c5f06485838d/jessie/Dockerfile)

The packages in the `curl` and `scm` variants all have the same names in Alpine Linux as they do in the Debian/Ubuntu source. The translation of packages for the `latest` image is a bit more complicated, though. The packages used are listed below:

| **buildpack-deps**     | **alpine-buildpack-deps**   |
|------------------------|-----------------------------|
| `autoconf`             | `autoconf`                  |
| `automake`             | `automake`                  |
| `bzip2`                | `bzip2`                     |
| `file`                 | `file`                      |
| `g++`                  | `g++`                       |
| `gcc`                  | `gcc`                       |
| `imagemagick`          | `imagemagick-dev`           |
| `libbz2-dev`           | `bzip2-dev`                 |
| `libc6-dev`            | `libc-dev`, `linux-headers` |
| `libcurl4-openssl-dev` | `curl-dev`                  |
| `libdb-dev`            | `db-dev`                    |
| `libevent-dev`         | `libevent-dev`              |
| `libffi-dev`           | `libffi-dev`                |
| `libgdbm-dev`          | `gdbm-dev`                  |
| `libgeoip-dev`         | `geoip-dev`                 |
| `libglib2.0-dev`       | `glib-dev`                  |
| `libjpeg-dev`          | `jpeg-dev`                  |
| `libkrb5-dev`          | `krb5-dev`                  |
| `liblzma-dev`          | `xz-dev`                    |
| `libmagickcore-dev`    | `imagemagick-dev`           |
| `libmagickwand-dev`    | `imagemagick-dev`           |
| `libmysqlclient-dev`   | `mariadb-dev`*              |
| `libncurses-dev`       | `ncurses-dev`               |
| `libpng-dev`           | `libpng-dev`                |
| `libpq-dev`            | `postgresql-dev`*           |
| `libreadline-dev`      | `readline-dev`              |
| `libsqlite3-dev`       | `sqlite-dev`                |
| `libssl-dev`           | `openssl-dev`               |
| `libtool`              | `libtool`                   |
| `libwebp-dev`          | `libwebp-dev`               |
| `libxml2-dev`          | `libxml2-dev`               |
| `libxslt-dev`          | `libxslt-dev`               |
| `libyaml-dev`          | `yaml-dev`                  |
| `make`                 | `make`                      |
| `patch`                | `patch`                     |
| `xz-utils`             | `xz`                        |
| `zlib1g-dev`           | `zlib-dev`                  |

\*Alpine Linux doesn't have development packages for MySQL or PostgreSQL that include only the headers/libraries necessary for client-side libraries. These Alpine packages are quite large because they include server headers/libraries as well.
