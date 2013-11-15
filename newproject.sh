#!/bin/bash
#source ~/.profile
#cd ~
cd ~/sites
mkvirtualenv --no-site-packages django-$1-env
pip install Django
django-admin.py startproject --template https://bitbucket.org/grialexey/django-project-template/get/master.zip $1
cd $1
pip install -r requirements.txt
pip freeze > requirements.txt
cp $1/settings/local-development.py $1/settings/local.py
python manage.py syncdb
python manage.py migrate
#python manage.py runserver
git init