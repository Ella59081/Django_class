Set up for Django project
---------------------------------------------------------
Create virtual environment - python -m venv .venv
Activate virtual environment - .venv\Scripts\activate
Install Django - pip install django
Create requirements.txt - pip freeze > requirements.txt
Install dependencies:
pip install djangorestframework djangorestframework-simplejwt psycopg[binary] python.env

Create the django project(config/project name) - django-admin startproject config .
Create an app - python manage.py startapp {app name}
Register app in config\settings.py, installed apps