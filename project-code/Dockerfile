FROM python:3-onbuild

RUN apt-get update
RUN apt-get install -y supervisor -q -y net-tools
RUN pip install requests
RUN pip install setuptools

COPY . /app 

WORKDIR /app

EXPOSE 8888
EXPOSE 9999

ENTRYPOINT ["make"]

