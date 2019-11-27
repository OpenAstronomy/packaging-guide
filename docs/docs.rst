.. _documentation:

Documenting your Package
========================

There are two main ways to document your project, both of
which are essential.

Docstrings
----------

First, public functions, methods, and classes
in your package should include *docstrings*, which are strings
attached to those objects which the user can access interactively
using e.g. ``help()`` and which can also be retrieved by automated
tools. See `PEP 257 - Docstring Conventions <https://www.python.org/dev/peps/pep-0257/>`_
for a high-level overview of what docstrings are. We recommend adopting
the `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`_
format for docstrings. An example of such a docstring is::

    def foo(var, long_var_name='hi'):
        """A one-line summary that does not use variable names.

        Several sentences providing an extended description. Refer to
        variables using back-ticks, e.g. `var`.

        Parameters
        ----------
        var : int
            The type above can either refer to an actual Python type
            (e.g. ``int``), or describe the type of the variable in more
            detail, e.g. ``(N,) ndarray`` or ``array_like``.
        long_var_name : {'hi', 'ho'}, optional
            Choices in brackets, default first when optional.

        Returns
        -------
        out : type
            Explanation of `out`.
        """

These docstrings should be included in the Python files alongside the Python
objects they document.

Narrative Documentation
-----------------------

Second, you should write a set of narrative documentation which functions as a
user guide, such as http://docs.astropy.org or http://docs.sunpy.org. For this
we recommend making use
of the `Sphinx <http://www.sphinx-doc.org/>`_ tool and storing your documentation
inside a ``docs`` directory.

To set this up, first install the Sphinx package, then create a ``docs`` directory
and run ``sphinx-quickstart`` inside it::

    $ mkdir docs
    $ cd docs
    $ sphinx-quickstart

We recommend answering ``n`` for the question of whether to separate
source and build directories. Once you have run this, you should see the following files
inside your ``docs`` directory::

    Makefile
    conf.py
    index.rst
    make.bat

The ``index.rst`` file is the root of your documentation. You can start writing content
in it and you can also start adding more ``.rst`` pages if needed. If you haven't used
Sphinx before, we recommend taking a look at their
`Getting Started <http://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ guide.
