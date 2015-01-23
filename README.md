Django project template
=======================

This Django project template uses Vagrant and Ansible IT Infrastructure tool

How to start a new project  
--------------------------
1. Switch to directory where you want to locate your new project;
2. Run this command (replace project_name with you know):  
   `django-admin.py startproject --template=https://bitbucket.org/grialexey/django-project-template/get/master.zip --name=Vagrantfile,installation.md,deployment.md,vars.yml project_name`  
3. Switch to project directory;
4. Edit `README.md` file. Add your project description in it;
5. Create repository:  
   `git init`  
   `git add .`  
   `git commit -m 'Initial commit'`
6. Push project in remote repository (github, bitbucket or another);
7. Follow instructions in `docs/installation.md` file to start development;
