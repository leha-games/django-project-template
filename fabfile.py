from contextlib import contextmanager
from fabric.api import local
from fabric.api import env
from fabric.api import *

PROJECTS_DIR = "~/sites"
PROFILE_FILE = "~/.profile"

def get_virtualenv_name(project_name):
	return "django-%s-env" % project_name

@contextmanager
def profile():
	with prefix("source %s" % PROFILE_FILE):
		yield

@contextmanager
def virtualenv(project_name):
    with profile(), prefix("workon %s" % get_virtualenv_name(project_name)):
        yield

@contextmanager
def projects_dir():
	with lcd(PROJECTS_DIR):
		yield

@contextmanager
def project_root_dir(project_name):
	with projects_dir(), lcd(project_name):
		yield

@contextmanager
def project_base_dir(project_name):
	with project_root_dir(project_name):
		with lcd(project_name):
			yield

def django_set_settings(project_name, environment):
	with project_base_dir(project_name):
		local("cp settings/local-%s.py settings/local.py" % environment)

def make_db_dir(project_name):
	with project_root_dir(project_name):
		local("mkdir db")

def make_project_docs_dir(project_name):
	with project_root_dir(project_name):
		local("mkdir project-docs")		

def django_syncdb(project_name):
	with project_root_dir(project_name), virtualenv(project_name):
		local("python manage.py syncdb")

def django_migrate(project_name):
	with project_root_dir(project_name), virtualenv(project_name):
		local("python manage.py migrate")

def git_init(project_name):
	with project_root_dir(project_name):
		local("git init")

def git_add_all(project_name):
	with project_root_dir(project_name):
		local("git add .")

def git_commit(project_name, commit_message):
	with project_root_dir(project_name):
		local("git commit -m '%s'" % commit_message)

def git_add_tag(project_name, annotated_tag, message):
	with project_root_dir(project_name):
		local("git tag -a '%s' -m '%s'" % (annotated_tag, message))

def git_initialization(project_name):
	git_init(project_name)
	git_add_all(project_name)
	git_commit(project_name, 'Initial commit')
	git_add_tag(project_name, '0.1.0', 'Version 0.1.0')

def pip_install_requirements(project_name, requirements_file="requirements.txt"):
	with project_root_dir(project_name), virtualenv(project_name):
		local("pip install -r %s" % requirements_file)

def pip_freeze_requirements(project_name, requirements_file="requirements.txt"):
	with project_root_dir(project_name), virtualenv(project_name):
		local("pip freeze > %s" % requirements_file)

def pip_install_package(project_name, package_name):
	with virtualenv(project_name):
		local("pip install %s" % package_name)

def django_start_project(project_name, project_template="https://bitbucket.org/grialexey/django-project-template/get/master.zip"):		
	with projects_dir(), virtualenv(project_name):
		# todo: if no template (template in constraints)
		local("django-admin.py startproject --template %s %s" % (project_template, project_name))

def make_virtual_env(project_name):
	with profile():
		# todo: --no-site-packages optional
		local("mkvirtualenv --no-site-packages %s" % get_virtualenv_name(project_name))

def create_database(project_name):
	make_db_dir(project_name)
	django_syncdb(project_name)
	django_migrate(project_name)

def new_project(project_name):
	make_virtual_env(project_name)
	pip_install_package(project_name, "Django")
	django_start_project(project_name)
	pip_install_requirements(project_name)
	pip_freeze_requirements(project_name)
	django_set_settings(project_name, "development")
	create_database(project_name)
	make_project_docs_dir(project_name)
	git_initialization(project_name)
