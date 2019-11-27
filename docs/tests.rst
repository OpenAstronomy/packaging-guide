.. _testing:

Testing your package
====================

While writing new functionality for your package, you should also make sure that
you write unit tests. We suggest using the `pytest <https://docs.pytest.org/>`_
framework for writing and running tests.

Where to keep tests
-------------------

We recommend placing the tests inside sub-folders called ``tests`` alongside the
Python code they are meant to test - for example, the layout of the package might
look like::

    my_package/__init__.py
    my_package/utils.py
    my_package/tests/__init__.py
    my_package/tests/test_utils.py

The name of the test files should start with ``test_``. We recommend taking a look
at the `Getting Started <https://docs.pytest.org/en/latest/getting-started.html>`_
guide for pytest for how to write tests, as well as the `Astropy guide on writing
tests <http://docs.astropy.org/en/stable/development/testguide.html#writing-tests>`_.

Running tests
-------------

Assuming you have installed pytest, the easiest way to run the tests is to run the
``pytest`` command::

    pytest my_package

Note that if your package contains C extension, you will need to make sure the
extensions are compiled ahead of time - you can either do this with::

    python setup.py build_ext --inplace

or with::

    pip install -e .

Once you have done this, the pytest command should work. If your package defines
entry points, you will likely need to run the ``pip`` command if you are running
tests that rely on the entry points.

Defining default pytest options
-------------------------------

If you regularly need to run tests with the same command-line flags for your
package, or if you want to set options that are required for certain pytest
plugins, you can control these by adding a ``[tool:pytest]`` section to your
``setup.cfg`` file, for example::

    [tool:pytest]
    addopts = -v

will ensure that tests are always run in verbose mode.

Running doctests
----------------

It is possible to use pytest to run doctests (blocks of code in docstrings or in
the .rst docs) as part of the test suite. If you want to do this, we recommend
using the `pytest-doctestplus <https://github.com/astropy/pytest-doctestplus>`
plugin. You can define the following options in your ``setup.cfg`` file to make
sure that this option is always enabled::

    [tool:pytest]
    doctest_plus = enabled
    addopts = --doctest-rst

Declaring dependencies for tests
--------------------------------

To make it easier for contributors to get set up with the dependencies
required to run the tests, as well as to make it easier to
configure automated builds (with e.g. :ref:`tox <tox>`), you should
define an ``[options.extras_require]`` section in
your ``setup.cfg`` file named ``test`` which lists the dependencies
required to run the tests (not including dependencies already
mentioned in ``install_requires``)::

    [options.extras_require]
    test =
        pytest
        pytest-doctestplus

This will then allow contributors to type::

    pip install -e .[test]

to install the package in developer/editable mode along with the test
dependencies.
