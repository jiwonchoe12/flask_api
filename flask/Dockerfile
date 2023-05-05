FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3.8 python3-pip
RUN pip3 install -r requirements.txt
RUN pip3 install PyMySQL


CMD ["uwsgi", "uwsgi.ini"]
