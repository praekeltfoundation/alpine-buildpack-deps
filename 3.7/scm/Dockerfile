FROM praekeltfoundation/alpine-buildpack-deps:3.7-curl

# procps is very common in build systems, and is a reasonably small package
RUN apk add --no-cache \
        bzr \
        git \
        mercurial \
        openssh-client \
        subversion \
        \
        procps
