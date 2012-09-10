mkvirtualenv --no-site-packages django-PROJECTNAME-env
pip install Django
django-admin.py startproject --template https://bitbucket.org/grialexey/django-project-template/get/master.zip PROJECTNAME
cd PROJECTNAME
#Select your database adapter in requirements.txt (MySQL)
pip install -r requirements.txt
cp PROJECTNAME/settings/local-dev.py PROJECTNAME/settings/local.py
python manage.py syncdb
python manage.py migrate
python manage.py runserver
git init