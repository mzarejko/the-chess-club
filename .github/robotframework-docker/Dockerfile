FROM python:3.8


ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip

RUN apt-get install -y libpq-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt install curl -y
RUN apt update

# install xvfb
RUN apt-get install -y wget xvfb unzip


RUN apt-get update && \
    apt-get install -y gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
    wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /chromedriver

# set display port and dbus env to avoid hanging
ENV DISPLAY=:99

ENV PATH=$PATH:/chromedriver

# install selenium
RUN pip install selenium


ENTRYPOINT ["robot"]

EXPOSE 5000
