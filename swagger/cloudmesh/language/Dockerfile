FROM ubuntu:16.04

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    #libssl-dev \
    zlib1g-dev \
    #libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    pandoc \
    wget \
    curl \
    #emacs \
    git-core \
    default-jre \
    software-properties-common -y
    
ENV HOME /
RUN git clone https://github.com/cloudmesh-community/hid-sp18-414.git
WORKDIR hid-sp18-414/swagger/cloudmesh/language

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

EXPOSE 8080

CMD git pull && make
