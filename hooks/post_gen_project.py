import sys
import pip
from getpass import getpass
import readline

# add modules that may be missing
pip.main(['install', 'github3.py', '--user'])
pip.main(['install', 'sh', '--user'])
pip.main(['install', 'requests', '--user'])

#import the modules TODO:add error trapping
from github3 import login, github, authorize
import sh

# create github repository
user = '{{cookiecutter.github_username}}'
password = '{{cookiecutter.github_password}}' # tried using getpass prompt doesn't come to user.
auth = authorize(user, password, ['repo', 'user'], "temp auth token for cookiecutter", '')
gh_token = auth.token
gh = login(token=gh_token)

repo = { 'name': '{{cookiecutter.repo_name}}', 'description': '{{cookiecutter.project_short_description}}' }

success = gh.create_repo(**repo)

# initilize and push the templated repo to the new github repo.
git = sh.git.bake(_cwd='.')
git.init()
git.add('--all')
git.commit(m='intial commit of {{cookiecutter.project_name}} templated from kylechamberlin/python3-cc-template using audreyr/cookiecutter')
git.remote('add', 'origin', 'git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.git')
git.push('--set-upstream', 'origin', 'master')

# scrutinizer init
import requests
import json

repo_name = json.dumps({"name": "{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}"})

requests.post('https://scrutinizer-ci.com/api/repositories.g?access_token={{cookiecutter.scrutinizer_token}}', data=repo_name)

# travis init

## travis is stupid and requires a github token to get a travis token!
travis_headers_pre_auth = {
         'User-Agent': 'Client2.2.2/2.2.2',
         'Accept': 'application/vnd.travis-ci.2+json',
         'Host': 'api.travis-ci.org',
         'Content-Type': 'application/json',
         'Content-Length': len(gh_token)
         }
travis_api_url = 'https://api.travis-ci.org'
travis_auth = requests.post(travis_api_url + '/auth/github', headers=travis_headers_pre_auth, data=json.dumps({'github_token': '{}'.format(gh_token)}))

travis_auth_token = json.loads(travis_auth.json)['access_token']

travis_headers_with_auth = {
        'User-Agent': 'Client2.2.2/2.2.2',
        'Accept': 'application/vnd.travis-ci.2+json',
        'Host': 'api.travis-ci.org',
        'Content-Type': 'application/json',
        'Authorization': 'token {}'.format(travis_auth_token)
        }

repo_info = requests.get(travis_api_url + '/repos/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}'
requests.put(travis_api_url + '/hooks', headers=travis_headers_with_auth, data=json.dumps
