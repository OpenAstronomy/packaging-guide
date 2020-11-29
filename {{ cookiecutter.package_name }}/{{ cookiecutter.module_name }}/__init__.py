# Licensed under a 3-clause BSD style license - see LICENSE.rst

{% if cookiecutter.setuptools_scm_git == 'y' %}
from .version import version as __version__
{% else %}
from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    pass
{% endif %}

{%- if cookiecutter.include_example_code == 'y' %}
from .example_mod import do_primes
# Then you can be explicit to control what ends up in the namespace,
__all__ = ['do_primes']
{% else %}
__all__ = []
{%- endif %}
