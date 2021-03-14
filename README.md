<h1 align="center">Welcome to django-jobs - A fork of djobs 👋</h1>

:cloud_with_snow: This repo illustrates how to port code from an older version of Django (1.5) to a more modern version (3.0). It's also a job board.

The GitHub Actions CI script is pretty shiny too. 

## :triangular_flag_on_post: Features

- Django 3.0.9
- click
- Docker
- Docker Compose
- environs[django]
- psycopg2-binary
- whitenoise

### :green_heart: CI

- black
- django-test-plus
- model-bakery
- pytest
- pytest-black
- pytest-django

### 🏠 [Homepage](https://github.com/jefftriplett/django-jobs)

## :wrench: Install

```shell
# Clone the repo
$ git clone https://github.com/jefftriplett/django-jobs/

# Change directory
$ cd django-jobs

# Rename the sample.env file to .env
$ mv sample.env .env
```

Create a virtual environment

## :rocket: Usage

```shell
# Run Django in background mode
$ docker-compose up -d

# Run Migrations
$ docker-compose run --rm web python manage.py migrate

# Run the server on http://localhost:8000/
$ docker-compose run --rm web python manage.py runserver

# Stop all running containers
$ docker-compose down

# Run Tests
$ docker-compose run --rm web pytest
```

## Show your support

Give a ⭐️ if this project helped you!
