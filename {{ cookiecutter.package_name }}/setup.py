#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os
{% if cookiecutter._provide_setuppy_fallback == 'y' -%}
import sys
{% endif -%}
from itertools import chain

from setuptools import setup
from setuptools.config import read_configuration
{% if cookiecutter.use_compiled_extensions == 'y' -%}

from extension_helpers import get_extensions
{% endif %}
{% if cookiecutter._provide_setuppy_fallback == 'y' -%}

################################################################################
# Raise helpful messages for old test and build_docs commands
################################################################################
test_help = """\
Running tests is no longer done using 'python setup.py test'.

Instead you will need to run:
    tox -e offline
if you don't already have tox installed, you can install it with:
    pip install tox
if you only want to run part of the test suite, you can also use pytest directly with:
    pip install -e .[dev]
    pytest
for more information, see:
  https://docs.sunpy.org/en/latest/dev_guide/tests.html
"""

if 'test' in sys.argv:
    print(test_help)
    sys.exit(1)

docs_help = """\
Building the documentation is no longer done using 'python setup.py build_docs'.

Instead you will need to run:
    tox -e build_docs
if you don't already have tox installed, you can install it with:
    pip install tox
for more information, see:
   https://docs.sunpy.org/en/latest/dev_guide/documentation.html#usage
"""

if 'build_docs' in sys.argv or 'build_sphinx' in sys.argv:
    print(docs_help)
    sys.exit(1)
{% endif -%}

################################################################################
# Programmatically generate some extras combos.
################################################################################
extras = read_configuration("setup.cfg")['options']['extras_require']

# Dev is everything
extras['dev'] = list(chain(*extras.values()))

# All is everything but tests and docs
exclude_keys = ("tests", "docs", "dev")
ex_extras = dict(filter(lambda i: i[0] not in exclude_keys, extras.items()))
# Concatenate all the values together for 'all'
extras['all'] = list(chain.from_iterable(ex_extras.values()))

################################################################################
# Version configuration and setup call
################################################################################

VERSION_TEMPLATE = """
# Note that we need to fall back to the hard-coded version if either
# setuptools_scm can't be imported or setuptools_scm can't determine the
# version, so we catch the generic 'Exception'.
try:
    from setuptools_scm import get_version
    __version__ = get_version(root='..', relative_to=__file__)
except Exception:
    __version__ = '{version}'
""".lstrip()

setup(
    extras_require=extras,
    use_scm_version={'write_to': os.path.join('{{ cookiecutter.module_name }}', 'version.py'),
                     'write_to_template': VERSION_TEMPLATE},
{% if cookiecutter.use_compiled_extensions == 'y' %}
    ext_modules=get_extensions()
{% endif %}
)
