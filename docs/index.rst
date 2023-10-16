Python Packaging Guide
======================

This guide is intended to explain modern Python packaging, it covers most of the core components of a modern package, and explains these components. It is broken up into the following sections:

.. toctree::
   :maxdepth: 2

   minimal
   docs
   tests
   tox
   extensions
   releasing
   scripts
   data
   ci
   advanced/index

Using the Template
==================

With this guide is a `cookiecutter <https://cookiecutter.readthedocs.io/>`__ template which allows you to get started quickly with a package as described in this guide.

To get started run:

.. code-block:: console

   $ pip install cookiecutter
   $ cookiecutter gh:OpenAstronomy/packaging-guide -o ./output_directory

This will create a new directory in your current directory named the same as the value of "packagename" you supplied.
Change into this directory and run ``git init`` to make it into a git repository.
This is required in order to have software versioning working for your package.

The goal of the template is to quickly get you setup with the files described in the guide.
The template currently implements the following optional flags, all of which default to off:

* ``include_example_code``: This option will fill your new package with some example functions to allow you to test it.
* ``use_compiled_extensions``: This turns on the features needed to support compiled extensions as described in :ref:`extensions`.
* ``enable_dynamic_dev_versions``: This enables a feature which ensures that ``my_package.__version__`` always returns the current git version as calculated by ``setuptools_scm`` when the package is installed as an editable install. See :ref:`dev-versions` for more details.
