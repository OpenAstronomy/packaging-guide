#!/usr/bin/env python
from setuptools import setup
{%- if cookiecutter.use_compiled_extensions == 'y' %}
from extension_helpers import get_extensions
{% endif -%}

{%- if cookiecutter.use_compiled_extensions == 'y' %}
setup(
    ext_modules=get_extensions()
)
{% endif -%}
