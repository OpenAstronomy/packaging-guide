from .version import version as __version__

from .example_mod import do_primes
{%- if cookiecutter.include_example_code == 'y' %}
# Then you can be explicit to control what ends up in the namespace,
__all__ = ['do_primes']
{% else %}
__all__ = []
{%- endif %}
