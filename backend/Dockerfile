FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONOTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install net-tools 
RUN apt-get install -y netcat

# wait tool for scheduling containers
COPY wait-for.sh wait-for.sh
RUN chmod +x wait-for.sh

COPY . /app/backend/

RUN useradd user
USER user

EXPOSE 8000


