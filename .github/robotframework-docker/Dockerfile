FROM gnahckire/python-selenium-chromedriver:latest


RUN apt-get update

RUN pip3 install --upgrade pip

RUN apt-get install libpq-dev -y

RUN apt update

COPY requirements.txt .
RUN pip install -r requirements.txt



ENTRYPOINT ["robot"]

EXPOSE 5000
