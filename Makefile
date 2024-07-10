# Makefile for Django project

# Variables
PYTHON = python3
PIP = pip3
PIP_COMPILE = pip-compile
DJANGO_ADMIN = django-admin
DJANGO_MANAGE = $(PYTHON) manage.py
VENV = venv
REQUIREMENTS = requirements.txt
REQUIREMENTS_DEV = requirements.dev.txt
REQUIREMENTS_IN = requirements.in
PROJECT_NAME = project
PRE_COMMIT = pre-commit

# Commands
RUNSERVER = $(DJANGO_MANAGE) runserver
MIGRATE = $(DJANGO_MANAGE) migrate
MAKEMIGRATIONS = $(DJANGO_MANAGE) makemigrations
COLLECTSTATIC = $(DJANGO_MANAGE) collectstatic
CREATESUPERUSER = $(DJANGO_MANAGE) createsuperuser
STARTPROJECT = $(DJANGO_ADMIN) startproject $(PROJECT_NAME) .
PRE_COMMIT_RUN = $(PRE_COMMIT) run --all-files
TEST = $(DJANGO_MANAGE) test
FLAKE8 = flake8

# Targets
.PHONY: runserver migrate makemigrations collectstatic createsuperuser test lint install requirements clean

help:
	@echo "Makefile commands:"
	@echo ""
	@echo "Usage:"
	@echo "  make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  help                Show this help message"
	@echo "  runserver           Run the Django development server"
	@echo "  migrate             Apply database migrations"
	@echo "  makemigrations      Create new database migrations"
	@echo "  collectstatic       Collect static files"
	@echo "  createsuperuser     Create a superuser for the Django admin"
	@echo "  test                Run Django tests"
	@echo "  lint                Lint the code using flake8"
	@echo "  install             Install Python dependencies from requirements.txt"
	@echo "  requirements        Freeze current dependencies to requirements.txt"
	@echo "  requirements.dev    Install Python dependencies from requirements.dev.txt"
	@echo "  compile             Compile requirements.in to requirements.txt"
	@echo "  clean               Remove Python cache files"
	@echo "  venv                Set up a Python virtual environment"
	@echo "  project             Start a new Django project"
	@echo "  pre-commit          Run pre-commit hooks on all files"
	@echo "  start               Initialize the virtual environment, install dependencies, and start the development server"

runserver:
	$(RUNSERVER)

migrate:
	$(MIGRATE)

makemigrations:
	$(MAKEMIGRATIONS)

collectstatic:
	$(COLLECTSTATIC)

createsuperuser:
	$(CREATESUPERUSER)

test:
	$(TEST)

lint:
	$(FLAKE8) .

install:
	$(PIP) install -r $(REQUIREMENTS)

requirements:
	$(PIP) freeze > $(REQUIREMENTS)

requirements_dev:
	$(PIP) install -r $(REQUIREMENTS_DEV)

compile:
	$(PIP_COMPILE) $(REQUIREMENTS_IN)

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

# To initialize and start a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/activate

project:
	$(STARTPROJECT)

pre-commit:
	$(PRE_COMMIT_RUN)

start: venv install project
	$(RUNSERVER)

fast_coverage:
	@echo "Running fast coverage check"
	@pytest --cov=blog_stack -n 4 --dist loadfile -q

coverage:
	pytest --cov=blog_stack --migrations -n 2 --dist loadfile

# Generate an image of the models in the system.
graph:
	python3 manage.py graph_models
