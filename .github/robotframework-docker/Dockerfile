FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip


RUN apt install libpq-dev -y
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt install curl -y
RUN apt update

# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

# Install chromedriver for Selenium
RUN curl wget https://chromedriver.storage.googleapis.com/78.0.3904.70/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver
RUN apt install default-jre

ENTRYPOINT ["robot"]

EXPOSE 8000
