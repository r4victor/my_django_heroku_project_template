# my_django_heroku_project_template

This repo is a blueprint for Django+DRF projects that I deploy on Heroku.

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
