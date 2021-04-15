FROM ruthvikc27/django-selenium:latest

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip


COPY requirements.txt .
RUN pip install -r requirements.txt



ENTRYPOINT ["robot"]

EXPOSE 5000
