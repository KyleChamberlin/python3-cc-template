import sys
import pip
from getpass import getpass
import readline

pip.main(['install', 'github3.py', '--user'])

from github3 import login, github

user = '{{ cookiecutter.github_username }}'

password = getpass('Github password for {0}: '.format(user))

gh = login(user, password)

repo = { 'name': '{{ cookiecutter.repo_name }}', 'description': '{{ cookiecutter.project_short_description }}' }

success = gh.create_repo(repo)


