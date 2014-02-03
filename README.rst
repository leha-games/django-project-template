To start new project enter:
django-admin.py startproject project-name --template=https://bitbucket.org/grialexey/django-project-template/get/master.zip --name=Vagrantfile


Starting development
--------------------
0. Don't forget to install vagrant plugins:
   `vagrant plugin install vagrant-cachier`
   `vagrant plugin install vagrant-vbguest`
   And download VBoxGuestAdditions.iso for your version of VirtualBox
1. Switch to project's directory
2. `vagrant up`
3. Uncomment line in Vagrantfile: 
   `config.vm.synced_folder ".", "/var/webapps/engus/code", owner: "engus", group: "engus"`
4. `vagrant reload`
3. `ansible-playbook deployment/deploy.yml -i deployment/hosts/development`
4. `vagrant ssh`
5. `sudo su -l engus`
5. `/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py createsuperuser`
6. `/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py runserver 0.0.0.0:8001`
7. localhost:8002

vagrant ssh
sudo su -l engus
/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py createsuperuser
/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py shell
/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py runserver 0.0.0.0:8001

/var/webapps/engus/virtualenv/bin/pip install <package>
/var/webapps/engus/virtualenv/bin/pip freeze > /var/webapps/engus/code/requirements.txt