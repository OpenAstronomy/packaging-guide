.. _documentation:

Documenting your Package
========================

There are two main ways to document your project, both of
which are essential: :ref:`docstrings` and :ref:`narrative`.

.. _docstrings:

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

.. _narrative:

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

.. _automodapi:

Including docstrings in the narrative documentation
---------------------------------------------------

As part of the narrative documentation, it is also common practice to include an
Application programming interface (API) page which lists the available classes,
methods, and functions in your package. Thankfully, if you've defined your docstrings
as described in :ref:`docstrings`, then this can be automated using the
`sphinx-automodapi <https://sphinx-automodapi.readthedocs.io>`_
package. See the documentation of that package for more details, but briefly,
you will need to add ``'sphinx_automodapi.automodapi'`` to the ``extensions``
variable in your ``conf.py`` file::

    extensions = ['sphinx_automodapi.automodapi']

In addition, if you use the numpydoc format for your docstrings, as recommended in :ref:`docstrings`,
you will need to include either ``'numpydoc'`` or ``'sphinx.ext.napoleon'`` in
the list of ``extensions`` (both packages provide a way to parse numpydoc-style
docstrings). If you use the numpydoc package, you will need to also include::

    numpydoc_show_class_members = False

in your ``conf.py`` file.

Declaring dependencies for documentation
----------------------------------------

To make it easier for contributors to get set up with the dependencies
required to build the documentation, as well as to make it easier to
configure automated builds (whether for :ref:`ReadTheDocs <readthedocs>`
or :ref:`tox <tox>`), you should define an ``[options.extras_require]`` section in
your ``setup.cfg`` file named ``docs`` which lists the dependencies
required to build the documentation (not including dependencies already
mentioned in ``install_requires``)::

    [options.extras_require]
    docs =
        sphinx
        sphinx-automodapi
        numpydoc

This will then allow contributors to type::

    pip install -e .[docs]

to install the package in developer/editable mode along with the documentation
dependencies.

.. _readthedocs:

Setting up ReadTheDocs
----------------------

`ReadTheDocs <http://readthedocs.org/>`_ is a platform that will build
docuemntation with sphinx and will then host it, and is used by many of
the Scientific Python packages. The easiest way to configure the build
is to add a file called ``.readthedocs.yml`` to your package, and we
recommend starting off with::

    version: 2

    build:
    image: latest

    python:
    version: 3.7
    install:
        - method: pip
        path: .
        extra_requirements:
            - docs

Once you have added this to your repository, you can then import your
package into ReadTheDocs as described in `this guide
<https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_.
