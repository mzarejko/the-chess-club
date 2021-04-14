FROM zmwangx/docker-selenium-python:python-3.7-chromium-slim-stretch

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
RUN apt update
RUN apt install build-essential -y
RUN apt-get install libpq-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt


ENTRYPOINT ["robot"]

EXPOSE 8000
