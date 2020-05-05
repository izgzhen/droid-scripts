FROM openjdk:8
COPY dare /usr/src/tools/dare
WORKDIR /usr/src/tools

RUN apt-get update
RUN chmod a+x dare/dare-launcher-1.1.0
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y multiarch-support
RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
RUN apt-get install -y zlib1g:i386
