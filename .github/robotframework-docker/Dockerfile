FROM nicolasd86/docker-python-chromedriver:latest


ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

RUN apt-get install -y libpq-dev

COPY requirements.txt .
RUN pip install -r requirements.txt


ENTRYPOINT ["robot"]

EXPOSE 5000
