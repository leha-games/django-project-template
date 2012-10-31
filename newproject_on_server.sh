cd ~/private
/opt/python27/bin/virtualenv --no-site-packages django-$1-env
source ~/private/django-$1-env/bin/activate
pip install django
cd $1
pip install -r requirements.txt
cp $1/settings/local-prod.py $1/settings/local.py
pip install mysql-python
python manage.py syncdb
python manage.py migrate
python manage.py collectstatic

