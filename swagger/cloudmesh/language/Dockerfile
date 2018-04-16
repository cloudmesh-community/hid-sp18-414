FROM ubuntu:16.04
RUN apt-get update -qy
RUN apt-get install -qy \
    git \
    wget \
    make \
    default-jre \
    python-pip
ENV HOME /
RUN git clone https://github.com/cloudmesh-community/hid-sp18-414.git
WORKDIR hid-sp18-414/swagger/cloudmesh/language
RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
EXPOSE 8080
CMD git pull && make
