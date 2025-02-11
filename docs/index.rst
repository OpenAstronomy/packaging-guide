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

To create a new package based on the template run:

.. code-block:: console

   $ pip install cookiecutter cruft
   $ cruft create https://github.com/sunpy/package-template

and go through the steps offered in the cli naming your package and filling in your details.
Cruft is built on cookiecutter, and enables the updating of the template from the source.
This takes the form of pull requests to the repository that the new package is pushed to.
If a package already has a cookiecutter template, it can be linked to the parent repository using ``cruft link url-to-template``.

To manually check whether the current environment matches with the template then ``cruft check`` will tell you what the current status is.
``cruft update`` will manually trigger an updating of the package to the template.

If you would like to stick to simply the cookiecutter approach, the template still supports that functionality thusly:

.. code-block:: console

   $ pip install cookiecutter
   $ cookiecutter gh:sunpy/package-template -o ./output_directory

This will create a new directory in your current directory named the same as the value of "packagename" you supplied.
Change into this directory and run ``git init`` to make it into a git repository, and make an initial commit.
This is required in order to have software versioning working for your package.

The goal of the template is to quickly get you setup with the files described in the guide.
The template currently implements the following optional flags, all of which default to off:

* ``include_example_code``: This option will fill your new package with some example functions to allow you to test it.
* ``use_compiled_extensions``: This turns on the features needed to support compiled extensions as described in :ref:`extensions`.
* ``enable_dynamic_dev_versions``: This enables a feature which ensures that ``my_package.__version__`` always returns the current git version as calculated by ``setuptools_scm`` when the package is installed as an editable install. See :ref:`dev-versions` for more details.
* ``include_cruft_update_github_repo``: This option adds a github workflow with pulls in the latest changes from the template every Monday morning and creates a PR against the repo which can then be accepted or closed.
* ``use_extended_ruff_linting``: This option flag enables the stricter ruff rules. Recommend `Y` on creation of a new project.

Pre-commit
==========

Pre-commit is configured through ``.pre-commit-config.yaml`` and can be installed locally and ran:

.. code-block:: bash

    $ pre-commit run --all-files

It also possible to use the tox environment to run it and and is integrated into the CI.

Within ``.pre-commit-config.yaml``, there are several tools and each one is configured either within the ``.pre-commit-config.yaml`` or for larger tools like ruff, it is has a dedicated config file ``.ruff.toml`` and we strongly recommend using the full set of rules when you setup your package.

Updating to a new version of the template
=========================================

It will be simplest to updating a package to a newer template by waiting for the GitHub workflow to trigger.
This will trigger a pull request one can review and merge via GitHub's UI.

If you do not want to wait, or want to do it manually, you will have to use cruft's CLI.
For this you will need to install cruft locally and then you can check the status of the package by running:

.. code-block:: bash
    $ cruft check

This will let you know whether the repository is up to date or not.
From there, you can run:

.. code-block:: bash
    $ cruft update

To update the repo and if there is a case conflicting files, ``.rej`` files will be created and you will have to manually deal with them and merge changes.

If you need up update one of the variables in the package ``.cruft.json`` for example, changing a ``n`` to a ``` this can be done using:

.. code-block:: bash
    $ cruft update --variables-to-update '{"use_extended_ruff_linting": "y"}'

This will work through the codebase and include the desired functionality without any further action.
Then you can commit and push the resulting changes.
