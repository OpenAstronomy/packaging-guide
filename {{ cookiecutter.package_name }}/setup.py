#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from setuptools import setup
{% if cookiecutter.use_compiled_extensions == 'y' %}
from extension_helpers import get_extensions
{% endif %}

setup(
{% if cookiecutter.setuptools_scm_git == 'y' %}
    use_scm_version={'write_to': os.path.join(
        '{{ cookiecutter.module_name }}', '_version.py')},
{% else %}
    use_scm_version=True,
{% endif %}

{% if cookiecutter.use_compiled_extensions == 'y' %}
    ext_modules=get_extensions()
{% endif %}
)
