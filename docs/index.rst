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


Using the Template
==================

With this guide is a `cookiecutter <https://cookiecutter.readthedocs.io/>`__
template which allows you to get started quickly with a package as described in
this guide. To use this, we recommend you use the `pieceofcake
<https://pypi.org/project/pieceofcake/>`__ wrapper which gives you more details
on the questions.

To get started run:

.. code-block:: console

   $ pip install pieceofcake
   $ pieceofcake gh:OpenAstronomy/packaging-guide ./output_directory

