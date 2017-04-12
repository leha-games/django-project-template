Django project template
=======================

This Django project template uses Vagrant and Ansible IT Infrastructure tool

How to start a new project  
--------------------------
1. Django must be installed on your system;
2. Switch to directory where you want to locate your new project;
3. Run this command (replace project_name with you know):  
   `django-admin.py startproject --template=https://github.com/grialexey/django-project-template/archive/master.zip --name=Vagrantfile,installation.md,deployment.md,vars.yml,create_development_database.sql,DJANGO_DATABASE_USER_NAME,DJANGO_DATABASE_NAME django_project_name`  
4. Switch to project directory;
5. Edit `README.md` file. Add your project description in it;
6. Create repository:  
   `git init`  
   `git add .`  
   `git commit -m 'Initial commit'`
7. Force add `deployment/credentials/development/` and `deployment/hosts/development` in your repository;
7. Push project in remote repository (github, bitbucket or another);
8. Follow instructions in `docs/installation.md` file to start development;
