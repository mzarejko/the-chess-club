# the chess club

## Goal


## Content

1. [General Info](#info)
2. [Technologies](#Technologies)
3. [Setup](#Setup)
4. [Status](#Status)


## General info <a name="info"></a>

All docker are for CI/CD with robotframework, if you work locally do not touch them!

## Technologies <a name="technologies"></a>
     

## Build


Next you need file .env in backend/base/ with important secrets like passwords or keys.

     POSTGRES_HOST = 'name of database host (localhost can't by set for dockers)',
     PORT = 5432,
     POSTGRES_DB = 'name of database',
     POSTGRES_USER = 'username',
     POSTGRES_PASSWORD = 'password',
     
After performing all steps above you can launch backend, frontend and database by typing command below:

     $ docker-compose up --build

This will load all modules in the correct order thenks to the bash script [wait.for.sh](./backend/wait-for.sh).
After few seconds site will work at address http://0.0.0.0:8000/ as backend and at http://0.0.0.0:3000/ as frontend.



Installation assumes that you already have the [postgreSQL](https://www.postgresql.org/download/) installed on computer. 
While launching, website have to connect to local database with special parametrs like below:

     POSTGRES_HOST = 'localhost',
     POSTGRES_DB = 'chessbase',
     POSTGRES_USER = 'owner',
     POSTGRES_PASSWORD = 'harnas',

Example of setting database for website:


In program [psql](https://www.postgresql.org/docs/9.2/app-psql.html) create database with name chessbase:

    user=# CREATE DATABASE chessbase;

Next create user owner:

    user=# CREATE USER owner WITH ENCRYPTED PASSWORD 'harnas';

Grant privileges to created user.

    user=# GRANT ALL PRIVILEGES ON DATABASE chessbase TO owner;

After performing this actions website can connect with postgres, before starting program it need special
environment listed in file [requirements.txt](./backend/requirements.txt) which can be installed by python 3.8:

First create virtual env:

     $ python3 -m venv chessgame
     
Install in this environment all libraries by file in /backend/:

    $ pip install -r requirements.txt

if everything was done successfully, you can run backend separately.

    $ python manage.py runserver

If you need launch it with deployment environment you need type:

    $ python manage.py runserver --settings=base.production

This command need all parameters accessible by os.environ


To start frontend you have to install [node and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm), next type command in /frontend/:

    $ npm start


## Status <a name="Status"></a>

  - [ ]  registration/login
  - [ ]   token JWT management (sliding session technique)
  - [ ]   exceptions management
  - [ ]   production on the herok cloud
 
