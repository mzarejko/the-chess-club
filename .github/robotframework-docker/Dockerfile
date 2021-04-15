FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get update

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


# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION 87.0.4280.88
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR


# Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR


# Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH


ENTRYPOINT ["robot"]

EXPOSE 8000
