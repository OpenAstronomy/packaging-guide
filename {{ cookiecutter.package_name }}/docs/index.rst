{{ cookiecutter.package_name }} Documentation
{{ '-' * (cookiecutter.package_name + " Documentation")|length }}

This is the documentation for {{ cookiecutter.package_name }}.

.. toctree::
   :maxdepth: 2

   whatsnew/index


Reference/API
=============

.. automodapi:: {{ cookiecutter.package_name }}
