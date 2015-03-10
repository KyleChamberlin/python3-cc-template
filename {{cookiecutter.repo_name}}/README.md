{{cookiecutter.project_name}}
======

{{cookiecutter.project_short_description}}

[![Build Status](http://img.shields.io/travis/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/master.svg)](https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}})
[![Coverage Status](http://img.shields.io/coveralls/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/master.svg)](https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}})
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.svg)](https://scrutinizer-ci.com/g/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/{{cookiecutter.pkg_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.pkg_name}})
[![PyPI Downloads](http://img.shields.io/pypi/dm/{{cookiecutter.pkg_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.pkg_name}})


Getting Started
===============

Requirements
------------

* Python {{ cookiecutter.python_major_version }}.{{ cookiecutter.python_minor_version }}+

Installation
------------

{{cookiecutter.project_name}} can be installed with pip:

```
$ pip install {{cookiecutter.pkg_name}}
```

or directly from the source code:

```
$ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.git
$ cd {{cookiecutter.repo_name}}
$ python setup.py install
```

Basic Usage
===========

After installation, the package can imported:

```
$ python
>>> import {{cookiecutter.pkg_name}}
>>> {{cookiecutter.pkg_name}}.__version__
```

{{cookiecutter.project_name}} doesn't do anything, it's a template.

For Contributors
================

Requirements
------------

To install any dependencies simply run:

```
$ pip install -r requirements.txt
```

Installation
------------

Create a virtualenv:

```
$ make env
```

Run the tests:

```
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```
$ make dist  # dry run
$ make upload
```
