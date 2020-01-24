{{ cookiecutter.package_name }} Documentation
{{ '-' * cookiecutter.package_name + "Documentation"|length }}

This is the documentation for {{ cookiecutter.package_name }}.
{{ cookiecutter.long_description|wordwrap(break_long_words=False) }}

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
