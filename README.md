# the chess club

## Goal


## Content

1. [General Info](#info)
2. [Technologies](#Technologies)
3. [Setup](#Setup)
4. [Status](#Status)


## General info <a name="info"></a>


## Technologies <a name="technologies"></a>
     

## Build

### Setup with dockers

To lanuch program you must install the [docker-engine](https://docs.docker.com/engine/install/) with [docker-compose](https://docs.docker.com/compose/install/). 
Dockers in this project are prepared only for linux systems so if you use Windows, you will need [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or some other virtual machine.


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


### Setup without dockers

This part assumes that you already have the [postgres database](https://www.postgresql.org/download/) installed on computer and you don't want use dockers. 
You need file .env like in first install or you can change all settings in django by yourself in /backend/development.
After this actions to launch program you have to create database with settings which you specified in the .env file or in the code.

Examle of setting database:

File .env:

     POSTGRES_HOST = 'localhost' (other name will not work local install),
     PORT = 5432,
     POSTGRES_DB = 'chessbase',
     POSTGRES_USER = 'user',
     POSTGRES_PASSWORD = 'passwd',

In program [psql](https://www.postgresql.org/docs/9.2/app-psql.html):

    user=# CREATE DATABASE chessbase;


At the end program need special environment with libraries in [requirements.txt](./backend/requirements.txt) and python 3.8.

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
 
