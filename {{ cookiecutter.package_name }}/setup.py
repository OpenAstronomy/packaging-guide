#!/usr/bin/env python
{%- if cookiecutter.use_compiled_extensions == 'y' %}
from extension_helpers import get_extensions
{%- endif %}
from setuptools import setup

setup( {%- if cookiecutter.use_compiled_extensions == 'y' -%}
    ext_modules=get_extensions()
{%- endif -%} )
