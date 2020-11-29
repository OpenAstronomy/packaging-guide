#!/usr/bin/env python
from setuptools import setup
{% if cookiecutter.use_compiled_extensions == 'y' %}
from extension_helpers import get_extensions
{% endif %}

setup(
{% if cookiecutter.use_compiled_extensions == 'y' %}
    ext_modules=get_extensions()
{% endif %}
)
