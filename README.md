# alpine-buildpack-deps
An attempt at a "buildpack-deps"-like Docker image with Alpine Linux

### Images
The base image is the [official Docker Alpine image](https://hub.docker.com/_/alpine/).

This repo contains a set of images similar to the official [buildpack-deps](https://hub.docker.com/_/buildpack-deps/) images. It also includes a Python 2.7 "builder" image similar to the [official Python image](https://hub.docker.com/_/python/).

| **Tag**      | **Dockerfile location**               | **Base image** | **Description**                                       |
|--------------|---------------------------------------|----------------|-------------------------------------------------------|
| `curl`       | [`curl/Dockerfile`](curl/Dockerfile)  | `alpine:3.3`   | Alpine with `curl` and `wget`                         |
| `scm`        | [`scm/Dockerfile`](scm/Dockerfile)    | `:curl`        | `:curl` with version control tools                    |
| `latest`     | [`Dockerfile`](Dockerfile)            | `:scm`         | `:scm` with build tools                               |
| `python-2.7` | [`python/2.7/Dockerfile`](python/2.7/Dockerfile) | `:latest`      | Like the official `python` Docker image but on Alpine |
