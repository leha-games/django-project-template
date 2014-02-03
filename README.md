To start new project enter:  
`django-admin.py startproject project-name --template=https://bitbucket.org/grialexey/django-project-template/get/master.zip --name=Vagrantfile`


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
5. `ansible-playbook deployment/deploy.yml -i deployment/hosts/development`
6. `vagrant ssh`
7. `sudo su -l engus`
8. `/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py createsuperuser`
9. `/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py runserver 0.0.0.0:8001`
10. localhost:8002

Useful commands
---------------
`vagrant ssh`  
`sudo su -l engus`  
`/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py createsuperuser`  
`/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py shell`  
`/var/webapps/engus/virtualenv/bin/python /var/webapps/engus/code/manage.py runserver 0.0.0.0:8001`  

`/var/webapps/engus/virtualenv/bin/pip install <package>`  
`/var/webapps/engus/virtualenv/bin/pip freeze > /var/webapps/engus/code/requirements.txt`

Passwords crypt
---------------
`>>> openssl passwd -salt salty -1 mypass`


Initial remote server setup
---------------------------
`ansible-playbook deployment/initial.yml -i deployment/hosts/production --ask-pass -c paramiko`  
`ansible-playbook deployment/provision.yml -i deployment/hosts/production -K`  
`ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`


Production deploy
-----------------
`ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`