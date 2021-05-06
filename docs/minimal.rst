.. _minimal:

Minimal package layout
======================

To start off, we will take a look at the minimal set of files you will need to
create an installable Python package. Once you have set these up, your package
directory should look like::

    ├── LICENCE
    ├── MANIFEST.in
    ├── my_package
    │   └── __init__.py
    ├── pyproject.toml
    ├── README.rst
    ├── setup.cfg
    └── setup.py

where ``my_package`` is the name of your package. We will now take a look at all of
these files in turn.

.. _license:

LICENSE
-------

Assuming that you are planning to make your package open source, the most
important file you will need to add to your package is an open source license.
Many packages in the scientific Python ecosystem use the `3-clause BSD license
<https://opensource.org/licenses/BSD-3-Clause>`_ and we recommend following
this or using the `MIT license <https://opensource.org/licenses/MIT>`_
unless you have a good reason not to.

To include the license in your package, create a file called LICENSE
and paste the license text into it, making sure that you update the
copyright year, authors, and any other required fields

.. _readme:

README.rst
----------

Another important file to include is a README file, which briefly tells users
what the package is, and either gives some information about how to install/use
it or links to more extensive documentation. We recommend using the
`reStructuredText (rst) <http://docutils.sourceforge.net/rst.html>`_ format for
your README as this will ensure that the README gets rendered well online, e.g.
on `GitHub <https://github.com>`_ or `GitLab <https://gitlab.com>`_ and on `PyPI
<https://pypi.org>`_.

.. _package_init:

my_package/__init__.py
----------------------

Python code for your package should live in a sub-directory that has the name
of the Python module you want your users to import. This module name should
be a valid Python variable name, so cannot start with numbers and cannot include
hyphens. Valid package names are ``example`` or ``my_package``. For the rest
of this guide, we will assume the name of the module is ``my_package``.

Once you have created this directory, the first file to create in it should be a
file called ``__init__.py`` which will be the first code to be run when a user
imports your package. For now, the only information we will add to this file is
the version of the package, since users typically expect to be able to access
``my_package.__version__`` to find out the current package version. While you
could simply set e.g.::

    __version__ = '1.2'

in the ``__init__.py`` file, you then would need to make sure that the version
number is in sync with the version number defined in the :ref:`setup_cfg` file,
so a better approach is to put the following in your ``__init__.py`` file::

    from pkg_resources import get_distribution, DistributionNotFound
    try:
        __version__ = get_distribution(__name__).version
    except DistributionNotFound:
        pass

If you support Python 3.8 or higher only, you can replace the above with::

    from importlib_metadata import version as _version, PackageNotFoundError
    try:
        __version__ = _version(__name__)
    except PackageNotFoundError:
        pass

This will automatically set ``__version__`` to the global version of the package
declared in :ref:`setup_cfg` or set by the `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`__ package (see :ref:`setup_py` and
:ref:`pyproject` for more details).

.. _setup_cfg:

setup.cfg
---------

The ``setup.cfg`` file is where we will define the metadata about the package.
At a minimum, this file should contain the following (with the metadata updated
to that needed for your particular package)::

    [metadata]
    name = my-package
    description = My package description
    long_description = file: README.rst
    author = Your Name
    author_email = your@email.com
    url = https://link-to-your-project
    license = BSD 3-Clause License

    [options]
    zip_safe = False
    packages = find:
    install_requires =
        numpy
        astropy>=3.2

The ``name`` field is the name your package will have on PyPI. It is not necessarily
the same as the module name, so in this case we've set the package name to
``my-package`` even though the module name is ``my_package``. However, aside from
the case where the package name has a hyphen and the module name has an underscore,
we strongly recommend making the package and the module name the same to avoid confusion.

Note that the version of the package is **not** defined in the file above, because
we will be using the `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`_ package in the :ref:`setup_py`
and :ref:`pyproject` files (see those sections for more details). However, if
you choose to not use that package, you can also set the version in the
``[metadata]`` section using for example::

    version = 0.12

The ``description`` should be a short one-line sentence that will appear next to your package name
on `PyPI <https://pypi.org>`_ when users search for packages. The ``long_description``
is then set to be loaded from the ``README.rst`` file, and it will be rendered
nicely on the PyPI page for the package.

The ``zip_safe`` option should be set to ``False`` unless you understand the
implications of setting it to ``True`` - this option is most relevant when
producing application bundles with Python packages.

The ``packages`` line can be left as-is - this will automatically determine the
Python modules to install based on the presence of ``__init__.py`` files.

Finally, the ``install_requires`` section is important since it is where you will
be declaring the dependencies for your package. The cleanest way to do this is
to specify one package per line, as shown above. You can optionally include version
restrictions if needed (as shown with ``astropy>=3.2`` above. If your package has no dependencies then you don't need this option.

In the rest of this guide, we will discuss other options that can be added to
the ``setup.cfg`` file, but the above provide the minimal set you will need to
get started. For more information about what can go into a ``setup.cfg`` file,
you can also take a look at the `setuptools documentation
<https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files>`_.

.. TODO: optional dependencies

.. _setup_py:

setup.py
--------

The ``setup.py`` file used to be where a lot of the meta-data now defined in
the :ref:`setup_cfg` file used to be set, but when using :ref:`setup_cfg`, the
minimal ``setup.py`` file is very simple::

    from setuptools import setup
    setup(use_scm_version=True)

The ``use_scm_version`` option indicates that we want to use the `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`_ package to set the version
automatically based on git tags, which will produce version strings such as
``0.13`` for a stable release, or ``0.16.0.dev113+g3d1a8747`` for a developer
version.

In addition to this, there is a second version of ``setuptools_scm`` which is called ``setuptools_scm_git``.
This is turned off by default but if you enable it, it will reconfigure the ``setuptools_scm`` system to the following.
First a new folder ``{{ cookiecutter.package_name }}/{{ cookiecutter.module_name }}/_dev`` is added and ``scm_version.py`` file is added.
This file deals with the versioning instead of having ``setup.py`` write a ``_version.py`` to ``{{ cookiecutter.package_name }}/{{ cookiecutter.module_name }}``.
The benefit of this is so the git versioning works without adding in a runtime dependency on ``setuptools_scm``, you do not have relative imports and the versioning can break under `very specific packaging situations <https://github.com/astropy/astropy/issues/10760>`__.

.. _pyproject:

pyproject.toml
--------------

In :ref:`setup_cfg`, we discussed the ``install_requires`` option which can
be used to declare run-time dependencies for the package, which are
dependencies that are needed for the package to import and run correctly.
However, your package may have dependencies that are needed to build the
package in the first place. For example, the :ref:`setup_py` file shown
previously will only run correctly if both `setuptools
<https://setuptools.readthedocs.io>`_ and `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`_ are installed.

The recommended way to specify build-time dependencies is to create a file
called ``pyproject.toml`` which contains::

    [build-system]
    requires = ["setuptools", "wheel", "setuptools_scm"]
    build-backend = 'setuptools.build_meta'

If you choose to not use ``setuptools_scm``, you can remove it from this list.
If your package has C extensions that interface with `Numpy <https://numpy.org>`_,
you may also need to add Numpy to the above list - see :ref:`extensions` for
more details.

.. _manifest:

MANIFEST.in
-----------

The last file needed for a minimal set-up is the ``MANIFEST.in`` file,
which declares which files should be included when you release your
package (see :ref:`releasing` for more details about how to do this).
You don't need to declare all the files from the module directory or
standard files such as ``setup.py`` or ``setup.cfg``, so given the
files we've seen above you would need to include::

    include LICENSE
    include README.rst
    include pyproject.toml

You can find out more about the syntax of this file in
`Specifying the files to distribute <https://docs.python.org/3.8/distutils/sourcedist.html#specifying-the-files-to-distribute>`_
in the Python documentation.

If you do use ``setuptools_scm``, you have to be aware that **everything** that is git versioned will be included **by default**.
You will have to add::

    prune <folder or files>

to prevent this and slim down your final built package.
This important if you store test files or documentation and do not want to ship them in your final package.

Trying out your package
-----------------------

Once you have committed all of the above files to your repository, you
can test out the package by running::

    pip install .

from the root of the package. Once you have done this, you should be able to
start a Python session from a different directory and type e.g.::

    >>> import my_package
    >>> my_package.__version__
    0.1.dev1+g25976ae

.. TODO: mention about adding more files to package with functionality
