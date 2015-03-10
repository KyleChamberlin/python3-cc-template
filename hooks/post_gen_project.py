import sys
import pip
from getpass import getpass
import readline

pip.main(['install', 'github3.py', '--user'])

from github3 import login, Github

user = '{{ cookiecutter.github_username }}'

password = getpass('Github password for {0}: '.format(user))

github = login(user, password)

repo = { 'name': '{{ cookiecutter.repo_name }}', 'description': '{{ cookiecutter.project_short_description }}' }

success = github.create_repo(repo)


