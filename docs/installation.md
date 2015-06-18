Installation
============

Starting development
--------------------
0. Before anything else install Ansible, Vagrant, and two vagrant plugins:  
   `vagrant plugin install vagrant-cachier`  
   `vagrant plugin install vagrant-vbguest`  
   Download VBoxGuestAdditions.iso for your version of VirtualBox
1. Remove `192.168.33.10` from the `~/.ssh/known_hosts` (otherwise error can occur during provision);
2. Switch to project's directory;
3. Start vagrant:  
   `vagrant up`
4. Make a provision of project:  
   `ansible-playbook deployment/provision.yml -i deployment/hosts/development`
5. Uncomment this line in Vagrantfile to allow syncing a project directory:  
   `config.vm.synced_folder ".", "/var/webapps/{{ project_name }}/code", owner: "{{ project_name }}", group: "{{ project_name }}"`
6. Now you have to reload vagrant, to sync your project directory with virtual server:  
   `vagrant reload`
7. Set absolute paths in `deployment/hosts/` files  
7. Make a deploy of project:  
   `ansible-playbook deployment/deploy.yml -i deployment/hosts/development`
8. SSH to virtual server:  
   `vagrant ssh`
9. Switch to project user:  
   `sudo su -l {{ project_name }}`
10. Create website superuser with username `admin` and password `admin` for convention:  
   `/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py createsuperuser`
11. Freeze installed python packages in requirements.txt file:  
    `/var/webapps/{{ project_name }}/virtualenv/bin/pip freeze > /var/webapps/{{ project_name }}/code/requirements.txt`
12. Start django development server:  
    `/var/webapps/{{ project_name }}/virtualenv/bin/python /var/webapps/{{ project_name }}/code/manage.py runserver 0.0.0.0:8001`
13. Now you can see your app running in browser:  
    `http://127.0.0.1:8002/`
14. Install static files libs (preferably I do this from local machine, not from virtual server):
    `cd {{ project_name }}/static/frontend`  
    `sudo npm install --save-dev`  
    `bower install`


Initial remote server setup
---------------------------
1. Add files:  
   `credentials/production/super_user_name`  
   `credentials/production/super_user_password`  
   `credentials/production/super_user_password_crypted`  
   `credentials/production/project_user_password`  
   `credentials/production/project_user_password_crypted`  
   `credentials/production/ssh_port`  
   `deployment/hosts/initial`  
   `deployment/hosts/production`  
2. Edit `deployment/vars.yml` file. Pay attention to `server_hostname`, `project_repo` and `remote_host` variables
3. Generate `id_rsa` ssh key in `deployment/files/ssh/` directory by command (it asks you where to generate key):  
   `ssh-keygen -t rsa -C "grialexey@gmail.com"`  
4. Add public key `id_rsa.pub` in your repository, to allow server pull this repository.  
   This command can help:  
   `cat deployment/files/ssh/id_rsa.pub | pbcopy`
5. Do initial provision of server:  
   `ansible-playbook deployment/initial.yml -i deployment/hosts/initial --ask-pass -c paramiko`  
6. Update system packages and upgrade them if needed:  
   `ansible-playbook deployment/upgrade.yml -i deployment/hosts/production -K`  
7. Do project provision of server:  
   `ansible-playbook deployment/provision.yml -i deployment/hosts/production -K`  
8. Make first deploy of project:  
   `ansible-playbook deployment/deploy.yml -i deployment/hosts/production -K`
9. Login on remote server and create superuser;
10. Enjoy your project!

`sudo locale-gen ru_RU.UTF-8`
`sudo locale-gen en_US.UTF-8`



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
