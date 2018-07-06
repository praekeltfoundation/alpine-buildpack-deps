FROM praekeltfoundation/alpine-buildpack-deps:3.8-curl

# procps is very common in build systems, and is a reasonably small package
RUN apk add --no-cache \
        git \
        mercurial \
        openssh-client \
        subversion \
        \
        procps
