"""Package for {{cookiecutter.project_name}}."""

import sys

__project__ = '{{cookiecutter.project_name}}'
__version__ = '{{cookiecutter.version}}'
__email__ = '{{cookiecutter.email}}'

VERSION = __project__ + '-' + __version__

PYTHON_VERSION = {{cookiecutter.python_major_version}}, {{cookiecutter.python_minor_version}}

if not sys.version_info >= PYTHON_VERSION:  # pragma: no cover (manual test)
    exit("Python {}.{}+ is required.".format(*PYTHON_VERSION))
