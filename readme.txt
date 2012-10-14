mkvirtualenv --no-site-packages django-PROJECTNAME-env
pip install Django
django-admin.py startproject --template https://bitbucket.org/grialexey/django-project-template/get/master.zip PROJECTNAME
cd PROJECTNAME
# Select your database adapter in requirements.txt (MySQL)
pip install -r requirements.txt
cp PROJECTNAME/settings/local-dev.py PROJECTNAME/settings/local.py
python manage.py syncdb
python manage.py migrate
python manage.py runserver
git init
# Enter the admin panel and set django.contrib.sites site domain and name




On KOMTET.RU server: 
# upload project on the server in ~/private directory
# run "source newproject_on_server.sh PROJECTNAME"
cd ~/private
/opt/python27/bin/virtualenv --no-site-packages django-PROJECTNAME-env
source ~/private/django-PROJECTNAME-env/bin/activate
pip install django
cd PROJECTNAME
pip install -r requirements.txt
cp PROJECTNAME/settings/local-prod.py PROJECTNAME/settings/local.py
pip install mysql-python
python manage.py syncdb
python manage.py migrate
python manage.py collectstatic
# Enter the admin panel and set django.contrib.sites site domain and name
# Set django.fcgi and .htacccess files
