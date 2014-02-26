Django project template with Vagrant and Ansible 
================================================

To start new project enter:  
1. `django-admin.py startproject --template=https://bitbucket.org/grialexey/django-project-template/get/master.zip --name=Vagrantfile,README.md,vars.yml project_name`  
2. Edit deployment/vars.yml file
3. Create repository
4. Add files:
   `credentials/production/super_user_name`  
   `credentials/production/super_user_password`  
   `credentials/production/super_user_password_crypted`  
   `credentials/production/project_user_password`  
   `credentials/production/project_user_password_crypted`  
   `credentials/production/ssh_port`  
   `hosts/production`


Starting development
--------------------
0. Don't forget to install vagrant plugins:  
   `vagrant plugin install vagrant-cachier`  
   `vagrant plugin install vagrant-vbguest`  
   And download VBoxGuestAdditions.iso for your version of VirtualBox
1. Switch to project's directory
2. `vagrant up`
3. Uncomment line in Vagrantfile: 
   `config.vm.synced_folder ".", "/var/webapps/{{ project_name }}/code", owner: "{{ project_name }}", group: "{{ project_name }}"`
4. `vagrant reload`
5. `ansible-playbook deployment/deploy.yml -i deployment/hosts/development`
6. `vagrant ssh`
7. `sudo su -l {{ project_name }}`
8. `/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py createsuperuser`
9. `/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py runserver 0.0.0.0:8001`
10. localhost:8002

Useful commands
---------------
`vagrant ssh`  
`sudo su -l {{ project_name }}`  
`/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py createsuperuser`  
`/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py shell`  
`/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py runserver 0.0.0.0:8001`  

`/var/webapps/{{ project_name }}/virtualenv/bin/pip install <package>`  
`/var/webapps/{{ project_name }}/virtualenv/bin/pip freeze > /var/webapps/{{ project_name }}/code/requirements.txt`

Passwords crypt
---------------
`>>> openssl passwd -salt salty -1 mypass`


Initial remote server setup
---------------------------
create deployment/hosts/initial  
create deployment/hosts/production  
generate ssh key in deployment/files/ssh/ dir:  
`ssh-keygen -t rsa -C "grialexey@gmail.com"`  
add public key in BitBucket repository  
`ansible-playbook deployment/initial.yml -i deployment/hosts/initial --ask-pass -c paramiko`  
`ansible-playbook deployment/provision.yml -i deployment/hosts/production -K`  
bug with postgres  
solve by login by ssh and reinstall postgres:  
`sudo apt-get remove --purge postgresql-9.1`  
`sudo apt-get install postgresql-9.1`  
`ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`


Production deploy
-----------------
`ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`
