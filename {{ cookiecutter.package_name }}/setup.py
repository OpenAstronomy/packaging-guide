#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

import os

from setuptools import setup
{% if cookiecutter.use_compiled_extensions == 'y' %}
from extension_helpers import get_extensions
{% endif %}

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
    use_scm_version={'write_to': os.path.join('{{ cookiecutter.module_name }}', 'version.py'),
                     'write_to_template': VERSION_TEMPLATE},
{% if cookiecutter.use_compiled_extensions == 'y' %}
    ext_modules=get_extensions()
{% endif %}
)
