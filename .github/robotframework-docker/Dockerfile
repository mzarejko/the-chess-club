FROM robotframework/rfdocker:latest

ENV PYTHONUNBUFFERED 1

RUN apt install python3-pip	
RUN pip3 install --upgrade pip

RUN apt install libpq-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt


ENTRYPOINT ["robot"]

EXPOSE 8000
