# pandaid-api

[![Build Status](https://travis-ci.org/Pand-Aid /pandaid-api.svg?branch=master)](https://travis-ci.org/Pand-Aid /pandaid-api)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

REST API backend for Pand-Aid pandemic response app. Check out the project's [main page](hhttps://github.com/Pand-Aid/Main).

Please join us at the slack group [INSERT LINK]

# Prerequisites

- install [Docker](https://docs.docker.com/docker-for-mac/install/)  

## Homebrew installations:

```sh
$ brew install docker-compose
```

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
