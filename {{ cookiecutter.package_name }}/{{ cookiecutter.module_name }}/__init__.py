# Licensed under a 3-clause BSD style license - see LICENSE.rst

from .version import __version__

{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import do_primes
# Then you can be explicit to control what ends up in the namespace,
__all__ = ['do_primes']
{% else %}
__all__ = []
{%- endif %}
