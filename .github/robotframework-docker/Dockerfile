FROM nicholasvaliente/chromedriver-python:3.7

RUN pip3 install --upgrade pip

RUN apt-get install libpq-dev -y

RUN apt update

COPY requirements.txt .
RUN pip install -r requirements.txt


# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable


ENTRYPOINT ["robot"]

EXPOSE 5000
