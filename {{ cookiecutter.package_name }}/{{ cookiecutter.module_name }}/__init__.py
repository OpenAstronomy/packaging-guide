# Licensed under a 3-clause BSD style license - see LICENSE.rst

{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import do_primes
# Then you can be explicit to control what ends up in the namespace,
__all__ = ['do_primes']
{% else %}
__all__ = []
{%- endif %}
