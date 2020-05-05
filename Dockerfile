FROM ubuntu:xenial
COPY dare /usr/src/tools/dare
WORKDIR /usr/src/tools

RUN apt-get update

