FROM jamiehewland/alpine-buildpack-deps:curl

# procps is very common in build systems, and is a reasonably small package
RUN apk add --no-cache \
        bzr \
        git \
        mercurial \
        openssh-client \
        subversion \
        \
        procps
