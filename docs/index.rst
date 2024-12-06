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
   $ cruft create https://github.com/OpenAstronomy/packaging-guide

and go through the steps offered in the cli naming your package and filling in your details.
Cruft is built on cookiecutter, and enables the updating of the template from the source.
This takes the form of pull requests to the repository that the new package is pushed to.
If a package already has a cookiecutter template, it can be linked to the parent repository using ``cruft link url-to-template``.

To manually check whether the current environment matches with the template then ``cruft check`` will tell you what the current status is.
``cruft update`` will manually trigger an updating of the package to the template.

If you would like to stick to simply the cookiecutter approach, the template still supports that functionality thusly:

.. code-block:: console

   $ pip install cookiecutter
   $ cookiecutter gh:OpenAstronomy/packaging-guide -o ./output_directory

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

==========
Pre-commit
==========
Pre-commit is configured through `.ruff`, and can be installed locally as normal using `pre-commit run --all-files`.
However it is also run through tox, and is integrated into the CI, therefore it needs to be run though tox when you're checking it before PR.
As mentioned above, we have a strictly defined `.ruff.toml` and we strongly recommend using the full set of rules using the Y option in the setup wizard.

=====================================================
Updating a Package with a new version of the template
=====================================================

Updating the package can be performed either automatically though the GitHub workflow or automatically using crufts CLI tool.
Doing so thought the workflow is a case of reviewing a merging the PR through the GitHub interface.
Updating through the Cruft CLI is sometimes necessary, this is done using initially checking the status of the repo using `cruft check`.
This will let you know whether the repo is upto date or not.
If not, `cruft update` will update the repo, it is then a case of resolving any conflicts and clearing out any `.rej` files.
`.rej` files are artifacts of the cruft process.

If you need up explicitly update one of the variables in the package `.cruft.json` e.g. changing a `n` to a `y` this can be done using `variables_to_update`.
`cruft update --variables-to-update '{"use_extended_ruff_linting": "y"}`.
This will work through the repo and include the desired functionality without any further action.
Commit and push the resulting changes and you're done!
