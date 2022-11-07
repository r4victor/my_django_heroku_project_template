# my_django_heroku_project_template

This repo is a blueprint for Django + DRF + Postgres + Gunicorn API services to be deployed on Heroku.

## Overview

The `backend` folder is the output of `django-admin startproject` with minimal additions that almost any project requires:

* Basic dependencies such as `psycopg2` and `djangorestframework` included.
* Settings splitted for local and production environments and controlled by environment variables.
* Skeleton for views and tests.
* Common utilities.

There is also a bunch of files in the repo that help you with local development and deploying on Heroku.

## Usage

### Creating a new project

1. Clone this repo:

    ```
    git clone https://github.com/r4victor/my_django_heroku_project_template new_project && cd new_project
    ```

2. Init a new git folder:

    ```
    rm -r .git && git init
    ```

3. Create an `.env` file from the template:

    ```
    mv backend/.env-template backend/.env 
    ```

That's it! You have a new project set up!


### Local development

1. Create and activate a new Python virtual environment:

    ```
    python3 -m venv venv && source venv/bin/activate 
    ```

2. Install dependencies:

    ```
    pip install -r backend/requirements.txt
    ```

3. Set up a database. (You can use `scripts/setup_db.sh` script to do that). Then set `DATABASE_URL` in `.env`.

4. Specify the dev Django settings file:

    ```
    export DJANGO_SETTINGS_MODULE=backend.settings.dev
    ```

    Put this line in `venv/bin/activate` to set `DJANGO_SETTINGS_MODULE` automatically.

5. Run the Django server:

    ```
    cd backend && python manage.py runserver
    ```

### Deploying on Heroku

1. Create a new Heroku app and attach addons (e.g. Postgres).

2. Set the buildpack:

    ```
    heroku buildpacks:set https://github.com/negativetwelve/heroku-buildpack-subdir
    ```

3. Set required environment variables:

    ```
    heroku config:set DJANGO_SECRET_KEY='your_secret_key'
    heroku config:set DJANGO_ALLOWED_HOSTS='your_app_domain'
    ```

    To generate new `DJANGO_SECRET_KEY`, do:

    ```
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

3. Deploy!

    ```
    git push heroku master
    ```

## Miscellaneous

### nginx

Because of [the way Heroku does routing](https://devcenter.heroku.com/articles/http-routing#request-buffering) (routers do not buffer entire requests), serving your app with Gunicorn on Heroku is a bad idea if the app is user-facing. Slow clients can occupy all Gunicorn workers and make the app unavailable. The app becomes a subject to [the simplest DoS attack](https://en.wikipedia.org/wiki/Slowloris_(computer_security)).

To mitigate this, you can put nginx in front of Gunicorn. So you will have "Heroku Router -> nginx -> Gunicorn" setup. The [nginx](https://github.com/r4victor/my_django_heroku_project_template/tree/nginx) branch  of this repo contains modifications that add nginx.

Warning! I wasn't able to make [Heroku nginx buildpack](https://github.com/heroku/heroku-buildpack-nginx) work on the latest Heroku stack 22. It works on stack 20, so do

```
heroku stack:set heroku-20
```
