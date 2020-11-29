.. _tox:

Running Commands with Tox
=========================

`Tox <https://tox.readthedocs.io/en/latest/>`__ is a general purpose tool for
automating Python testing. We recommend using tox to specify the environments
in which your tests are run, both locally and on :ref:`ci` services.

Getting Started with Tox: Running tests
---------------------------------------

The first thing to configure tox to do is to run the tests for a package. The
most minimal tox file for a package following this guide is:

.. code-block:: ini

    [tox]
    envlist = py38
    isolated_build = True

    [testenv]
    extras = test
    commands = pytest {posargs}


Let's dig into the sections of this file, the ``[tox]`` section is the `global
configuration
<https://tox.readthedocs.io/en/latest/config.html#tox-global-settings>`__ for
the whole file. We use this to define ``envlist`` which is a list of all the
different builds configured in tox, here we set this to be a Python 3.8
environment, we will expand on this shortly. The ``isolated_build``
configuration option configures tox to build your source distribution in the
same manner as recommended in :ref:`releasing`.

The ``[testenv]`` section describes settings common to all environments you
specify in the tox file (unless they are later overridden), here we default
the ``commands =`` option to run pytest. The ``{posargs}`` is a tox
`substitution
<https://tox.readthedocs.io/en/latest/config.html#substitutions>`__ which
passes extra arguments through to ``pytest``. The ``extras = test`` line tells tox to install the dependencies listed in ``setup.cfg`` for running your test suite, this should include ``pytest``.

To run your tests with tox run:

.. code-block:: console

    $ tox -e py38

To pass arguments through to ``pytest`` use ``--`` here we tell pytest to
stop after the first failure.

.. code-block:: console

    $ tox -e py38 -- -x

Multiple builds
###############

Tox allows configuration of multiple builds in a few different ways, the
easiest one is to specify multiple Python versions in the env list:

.. code-block:: ini

    [tox]
    envlist = py{37,38}
    isolated_build = True

This takes our one test configuration and makes a Python 3.7 and a Python 3.8
environment that can be seen by listing all tox environments with:

.. code-block:: console

    $ tox -l
    py38
    py37

This feature is called `generative envlist <https://tox.readthedocs.io/en/latest/config.html#generative-envlist>`__ and can be used to create many build environments with minimal repetition.

Named Environments
##################

Using generative build environments you can define extra named environments
which can be useful for builds that need to specify specific dependencies or
settings. So far on this page we have assumed that all your dependencies are
specified in :ref:`setup_cfg`. You can extend or override this by using the
``deps =`` configuration option in tox. Here we define a named test
environment which installs the development version of numpy.

.. code-block:: ini

    [tox]
    envlist = py{37,38}{-numpydev,}
    isolated_build = True

    [testenv]
    extras = test
    commands = pytest {posargs}
    deps =
      numpydev: git+https://github.com/numpy/numpy


the ``envlist`` is now more complex, the result of this the following:

.. code-block:: console

    $ tox -l
    py37-numpydev
    py37
    py38-numpydev
    py38

with the ``deps`` overridden for ``numpydev`` builds.

Building Documentation with tox
-------------------------------

One common task which isn't running the test suite is building sphinx
documentation, documentation builds can be complex with a number of extra
dependencies or settings. In this section we will add a ``build_docs`` named
environment to tox. This section assumes you have already followed
:ref:`documentation`.

.. code-block:: ini

    [testenv:build_docs]
    extras = docs
    commands = sphinx-build docs docs/_build/html -W -b html {posargs}

This section installs the package extras for the documentation, which should
be a list of all your documentation dependencies and then sets the command to
be the `sphinx-build
<https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`__ command to
build the docs and output them in the ``docs/_build/html`` folder relative to
the ``tox.ini`` file.

You can now run your documentation with:

.. code-block:: console

    $ tox -e build_docs

you can pass through extra arguments to `sphinx-build
<https://www.sphinx-doc.org/en/master/man/sphinx-build.html>`__ because of
the ``{posargs}`` substitution. For example to force sphinx to ignore its
cache you can run:

.. code-block:: console

    $ tox -e build_docs -- -aE

Testing Packages with Compiled Extensions
-----------------------------------------

As configured in this guide so far, tox will perform the following actions (all in the same directory as the ``tox.ini`` file):

1. ``python setup.py sdist``
2. Create a new virtualenv
3. Install the built sdist.
4. Run the commands listed in ``commands =``, which here we assume to be ``pytest``.

(See https://tox.readthedocs.io/en/latest/index.html#system-overview for more details.)

For packages laid out as described in this guide, i.e. with the Python
package in a directory in the root repo, i.e. ``astropy/``, this means that
when ``pytest`` is run, it will collect the tests from the local directory
(as desired), and all imports of the package i.e. ``astropy`` will be
imported from the local directory *not the installed sdist*.

For pure python packages this generally isn't a problem, the contents of the
installed sdist and the local directory are the same (tox just made the sdist
from the local directory). However, for packages that include compiled
extensions, the installed package and the local directory are *not the same*.
The installed package has build the compiled extensions, and the local
directory does not. This means that unless you make some adjustments to the
package or the tox configuration compiled extensions will not work when
running pytest through tox as described above.

There are two main ways to alleviate this issue:

1. Move the Python package source code under a ``src/`` folder in the root of
the repo. This is a common package layout for Python projects, and it means
that you can not import your package relative to the git root, meaning it
will be imported from the installed sdist, see https://setuptools.readthedocs.io/en/latest/setuptools.html#using-a-src-layout for details.

2. Configure tox to run ``pytest`` from a temporary directory so that the
local import does not work. With this method you make use of pytest's
`--pyargs flag
<https://docs.pytest.org/en/latest/example/pythoncollection.html#interpreting-cmdline-arguments-as-python-packages>`__
to run the tests against the installed version of the package. This ensures
that any compiled extensions are properly detected, but prevents things like
specifying paths to pytest from working.

To configure tox to run ``pytest`` from a temporary directory do the
following in ``tox.ini``:


.. code-block:: ini

    [tox]
    envlist = py38
    isolated_build = True

    [testenv]
    changedir = tmp
    extras = test
    commands = pytest --pyargs packagename {posargs}

replacing ``packagename`` with the name of your package as you import it,
i.e. ``astropy``.
