FROM ubuntu:20.04

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/America/Bogota /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt update -y
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -y python3 python3-pip 

RUN chown www-data:www-data -R /usr/src/app

RUN apt-get install -y python3-pymysql

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt


ADD . /usr/src/app


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]