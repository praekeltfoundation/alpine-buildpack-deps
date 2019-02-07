# alpine-buildpack-deps

[![Docker Pulls](https://img.shields.io/docker/pulls/praekeltfoundation/alpine-buildpack-deps.svg)](https://hub.docker.com/r/praekeltfoundation/alpine-buildpack-deps/)
[![Build Status](https://img.shields.io/travis/praekeltfoundation/alpine-buildpack-deps/master.svg)](https://travis-ci.org/praekeltfoundation/alpine-buildpack-deps)

An attempt at a "buildpack-deps"-like Docker image with Alpine Linux

### Images
The base image is the [official Docker Alpine image](https://hub.docker.com/_/alpine/).

This repo contains a set of images similar to the official [buildpack-deps](https://hub.docker.com/_/buildpack-deps/) images.

| **Tag**  | **Base image** | **Description**                                               |
|----------|----------------|---------------------------------------------------------------|
| `curl`   | `alpine:3.x`   | Alpine with `curl` and `wget`                                 |
| `scm`    | `:curl`        | `:curl` with source control management (SCM) tools            |
| `latest` | `:scm`         | `:scm` with build tools and development libraries             |

## Caveats
* A best effort was made to find equivalent Alpine packages for the Debian packages in the official buildpack-deps. The packages may not always be *100% equivalent*.
* The code you're compiling in buildpack-deps could make assumptions about the host that are not necessarily true for Alpine Linux. For example:
  * That the standard Unix tools are the GNU implementations
  * That the standard C library is `glibc`
  * That the paths to development files are the Debian paths
* The default/`latest` tag for this image is ~~*not*~~ significantly smaller than the Debian/Ubuntu-based buildpack-deps images~~, although it is roughly the same size (~190MB compressed, ~660MB uncompressed). The reason for this is that the Alpine development libraries for PostgreSQL and MySQL are significantly bigger than the Debian ones.~~ If you are hoping to make a small "buildpack-deps"-based Docker image, you're probably doing Docker images wrong.

## Packages
The packages in the `curl` and `scm` variants mostly have the same names in Alpine Linux as they do in the Debian/Ubuntu source. The translation of packages for the `latest` image is a bit more complicated, though. The packages used are listed below.

### `curl`
[Upstream](https://github.com/docker-library/buildpack-deps/blob/9f60e19008458220114f1a0b6cd3710f1015d402/stretch/curl/Dockerfile)

| **buildpack-deps** | **alpine-buildpack-deps** |
|--------------------|---------------------------|
| `ca-certificates`  | `ca-certificates`         |
| `curl`             | `curl`                    |
| `dirmngr`          | `gnupg`                   |
| `gnupg`            | `gnupg`                   |
| `netbase`          | `alpine-baselayout`*      |
| `wget`             | `busybox`                 |

Additionally, we install the `tar` package in the `curl` image. This installs the GNU version of tar, which has more features than the BusyBox tar provided with Alpine Linux. In particular, the `--strip-components` option only available in GNU tar is commonly used in the Docker official images when extracting source code from tarballs.

\*This package is one of the base packages of Alpine Linux. It includes most of the `netbase` files including `/etc/protocols` and `/etc/services`.

### `scm`
[Upstream](https://github.com/docker-library/buildpack-deps/blob/1845b3f918f69b4c97912b0d4d68a5658458e84f/stretch/scm/Dockerfile)

| **buildpack-deps** | **alpine-buildpack-deps** |
|--------------------|---------------------------|
| `git`              | `git`                     |
| `mercurial`        | `mercurial`               |
| `openssh-client`   | `openssh-client`          |
| `procps`           | `procps`                  |
| `subversion`       | `subversion`              |

### `latest`
[Upstream](https://github.com/docker-library/buildpack-deps/blob/587934fb063d770d0611e94b57c9dd7a38edf928/stretch/Dockerfile)

| **buildpack-deps**     | **alpine-buildpack-deps**        |
|------------------------|----------------------------------|
| `autoconf`             | `autoconf`                       |
| `automake`             | `automake`                       |
| `bzip2`                | `bzip2`                          |
| `dpkg-dev`             | `dpkg`, `dpkg-dev`               |
| `file`                 | `file`                           |
| `g++`                  | `g++`                            |
| `gcc`                  | `gcc`                            |
| `imagemagick`          | `imagemagick-dev`                |
| `libbz2-dev`           | `bzip2-dev`                      |
| `libc6-dev`            | `libc-dev`, `linux-headers`      |
| `libcurl4-openssl-dev` | `curl-dev`                       |
| `libdb-dev`            | `db-dev`                         |
| `libevent-dev`         | `libevent-dev`                   |
| `libffi-dev`           | `libffi-dev`                     |
| `libgdbm-dev`          | `gdbm-dev`                       |
| `libgeoip-dev`         | `geoip-dev`                      |
| `libglib2.0-dev`       | `glib-dev`                       |
| `libjpeg-dev`          | `jpeg-dev`                       |
| `libkrb5-dev`          | `krb5-dev`                       |
| `liblzma-dev`          | `xz-dev`                         |
| `libmagickcore-dev`    | `imagemagick-dev`                |
| `libmagickwand-dev`    | `imagemagick-dev`                |
| `libmysqlclient-dev`   | `mariadb-dev`*                   |
| `libncurses5-dev`      | `ncurses-dev`                    |
| `libncursesw5-dev`     | `ncurses-dev`                    |
| `libpng-dev`           | `libpng-dev`                     |
| `libpq-dev`            | `postgresql-dev`*                |
| `libreadline-dev`      | `readline-dev`                   |
| `libsqlite3-dev`       | `sqlite-dev`                     |
| `libssl-dev`           | `openssl-dev`/(`libressl-dev`)** |
| `libtool`              | `libtool`                        |
| `libwebp-dev`          | `libwebp-dev`                    |
| `libxml2-dev`          | `libxml2-dev`                    |
| `libxslt-dev`          | `libxslt-dev`                    |
| `libyaml-dev`          | `yaml-dev`                       |
| `make`                 | `make`                           |
| `patch`                | `patch`                          |
| `unzip`                | `busybox`                        |
| `xz-utils`             | `xz`                             |
| `zlib1g-dev`           | `zlib-dev`                       |

\*Alpine Linux doesn't have development packages for MySQL or PostgreSQL that include only the headers/libraries necessary for client-side libraries. These Alpine packages are quite large because they include server headers/libraries as well.
\**Alpine Linux between versions 3.5 and 3.8 used LibreSSL. For version 3.9, they switched back to OpenSSL.
