# pandaid-api

[![Build Status](https://travis-ci.org/Pand-Aid /pandaid-api.svg?branch=master)](https://travis-ci.org/Pand-Aid /pandaid-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

REST API backend for Pand-Aid pandemic response app. Check out the project's [main page](hhttps://github.com/Pand-Aid/Main).

Please join us at the slack group [INSERT LINK]

# Prerequisites

- python 3.7 or higher 
- install [Docker](https://docs.docker.com/)  


# Local Development
All commands in bash regardless of operating system unless otherwise noted


## mac

### Homebrew installations:

```bash
$ brew install docker-compose
```
### setup
The first time you work on this, build the docker image:
```bash
docker-compose build
```

Then start it with 
```bash
docker-compose up
```

Then get a shell in the docker container and create a superuser

```
$ docker exec -ti pandaid-api_web_1 /bin/bash
:/code# python manage.py createsuperuser --email admin@example.com --username admin
```
## windows
### setup
The first time you work on this, build the docker image:
```bash
docker-compose build
```

Then start it with 
```bash
docker-compose up
```

Then get a shell in the docker container and create a superuser

```bash
$ winpty docker exec -it pandaid-api_web_1 //bin/sh
:/code# python manage.py createsuperuser --email admin@example.com --username admin
```

You can get an authentication token by sending a POST request to   `http://localhost:8000/api-token-auth/` with the superuser credentials in a formdata labeled `username` and `password`. # TODO be more clear and say how to use this 
## running

Start the dev server for local development:
```bash
docker-compose up
```

(hide server logs by adding the `-d` flag)

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
