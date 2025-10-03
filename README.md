# Django CRUD
This small project was meant to be a simple CRUD page with a REST API to test Django. It has Tailwindcss installed and is was done within the python's poetry dependency manager.

I've also added a docker-compose file to run a dockerized PostgreSQL container that should work perfectly with the project for testing and development.

> Remember to create a `.env` file inside de `django_project/` directory so that it runs as expected.

## For development
1. Install dependencies defined in `pyproject.toml` and create a virtual environment
```bash
$ poetry install
```

2. Activate venv or run commands from within
```bash
# If you have the poetry plugin installed, open a venv shell
$ poetry shell

# Run command within venv
$ poetry run
```

3. Run server and Tailwindcss compilation inside of the `django_project/` directory (two simultaneous shells)
```bash
# Run Django server
$ python manage.py runserver

# Run node compilation
$ npm run watch:css
```
