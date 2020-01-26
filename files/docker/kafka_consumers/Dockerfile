FROM python:3.7.5-buster

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="delsol_kafka_consumer"
LABEL maintainer="packetferret@gmail.com"
LABEL description="apache kafka consumer container"
LABEL license="GPLv2"
LABEL url="http://gitlab.home:8000/packetferret/delsol"
LABEL build-date="20191124"

### -------------------------------------------------
### Set environment
### -------------------------------------------------
ENV LANG C.UTF-8
ENV GPG_KEY 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D
ENV PYTHON_VERSION 3.7.5

### -------------------------------------------------
### Install packages
### -------------------------------------------------
RUN apt install -y gcc

### -------------------------------------------------
### Change directory to /home/tmp
### -------------------------------------------------
WORKDIR /home/tmp/

### -------------------------------------------------
### Add and install python packages
### -------------------------------------------------
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

### -------------------------------------------------
### Change directory to /home/python
### -------------------------------------------------
WORKDIR /home/python

### -------------------------------------------------
### Add python scripts
### -------------------------------------------------
ADD python/ /home/python

### -------------------------------------------------
### run python3
### -------------------------------------------------
CMD ["python3"]

