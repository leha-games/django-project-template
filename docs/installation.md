Installation
============

Starting development
--------------------
0. Don't forget to install vagrant plugins:  
   `vagrant plugin install vagrant-cachier`  
   `vagrant plugin install vagrant-vbguest`  
   And download VBoxGuestAdditions.iso for your version of VirtualBox
1. Remove `192.168.33.10` from the `~/.ssh/known_hosts` (otherwise can error occur during provision)
2. Switch to project's directory
3. Start vagrant and make provision:  
   `vagrant up`
4. Make a provision of project:  
   `ansible-playbook deployment/provision.yml -i deployment/hosts/development`
5. Uncomment line in Vagrantfile: 
   `config.vm.synced_folder ".", "/var/webapps/{{ project_name }}/code", owner: "{{ project_name }}", group: "{{ project_name }}"`
6. Now you have to reload vagrant, to sync your project directory with virtual server:  
   `vagrant reload`
7. Make a deploy of project:  
   `ansible-playbook deployment/deploy.yml -i deployment/hosts/development`
8. SSH to virtual server:  
   `vagrant ssh`
9. Switch to project user:  
   `sudo su -l {{ project_name }}`
10. Create supersuser with username `admin` and password `admin` for convention:  
   `/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py createsuperuser`
11. Freeze installed python packages in requirements.txt file:  
    `/var/webapps/{{ project_name }}/virtualenv/bin/pip freeze > /var/webapps/{{ project_name }}/code/requirements.txt`
12. Start django development server:  
    `/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py runserver 0.0.0.0:8001`
13. Now you can see your app running in browser:  
    `http://127.0.0.1:8002/`
14. Install static files libs (typically I do this from local machine, not from virtual server):
    `cd /var/webapps/{{ project_name }}/code/{{ project_name }}/static/frontend`  
    `npm install`  
    `bower install`


Initial remote server setup
---------------------------
1. Edit deployment/vars.yml file
2. Add files:
   `credentials/production/super_user_name`  
   `credentials/production/super_user_password`  
   `credentials/production/super_user_password_crypted`  
   `credentials/production/project_user_password`  
   `credentials/production/project_user_password_crypted`  
   `credentials/production/ssh_port`  
   `hosts/production`
3. create deployment/hosts/initial  
4. create deployment/hosts/production  
5. generate ssh key in deployment/files/ssh/ dir:  
6. `ssh-keygen -t rsa -C "grialexey@gmail.com"`  
7. add public key in BitBucket repository  
8. `ansible-playbook deployment/initial.yml -i deployment/hosts/initial --ask-pass -c paramiko`  
9. `ansible-playbook deployment/provision.yml -i deployment/hosts/production -K`  
10. `ansible-playbook deployment/upgrade.yml -i deployment/hosts/production -K`  
11. bug with postgres  
    solve by login by ssh and reinstall postgres:  
12. `sudo apt-get remove --purge postgresql-9.1`  
13. `sudo apt-get install postgresql-9.1`  
14. `ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`


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
