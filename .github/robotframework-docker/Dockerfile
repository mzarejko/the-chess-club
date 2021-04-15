FROM andreooi/robotframework-ubuntu:latest

# install python and pip
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y \
    python3.8 \
    python3-pip

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

RUN apt-get install -y build-essential libpq-dev python3-dev 

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt update


ENTRYPOINT ["robot"]

EXPOSE 5000
