# Licensed under a 3-clause BSD style license - see LICENSE.rst
{% if cookiecutter.enable_dynamic_dev_versions == 'y' %}
from .version import version as __version__
{% else %}
from .version import version as __version__
{% endif %}

{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import do_primes
# Then you can be explicit to control what ends up in the namespace,
__all__ = ['do_primes']
{% else %}
__all__ = []
{%- endif %}
