FROM selenium/standalone-chrome:89.0


RUN pip3 install --upgrade pip


RUN apt install libpq-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt install curl -y
RUN apt update

ENTRYPOINT ["robot"]

EXPOSE 8000
