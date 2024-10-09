@echo off

echo Running makemigrations...
python manage.py makemigrations

echo Running migrate...
python manage.py migrate

echo Starting server...
python manage.py runserver