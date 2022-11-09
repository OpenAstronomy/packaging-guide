.. _minimal:

Minimal package layout
======================

To start off, we will take a look at the minimal set of files you will need to
create an installable Python package. Once you have set these up, your package
directory should look like::

    ├── LICENCE
    ├── my_package
    │   └── __init__.py
    ├── pyproject.toml
    └── README.rst

where ``my_package`` is the name of your package. We will now take a look at all of
these files in turn.

.. _license:

``LICENSE``
-----------

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

``README.rst``
--------------

Another important file to include is a README file, which briefly tells users
what the package is, and either gives some information about how to install/use
it or links to more extensive documentation. We recommend using the
`reStructuredText (rst) <http://docutils.sourceforge.net/rst.html>`_ format for
your README as this will ensure that the README gets rendered well online, e.g.
on `GitHub <https://github.com>`_ or `GitLab <https://gitlab.com>`_ and on `PyPI
<https://pypi.org>`_.

.. _package_init:

``my_package/__init__.py``
--------------------------

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
could simply set e.g.

.. code-block:: python

    __version__ = '1.2'

in the ``__init__.py`` file, you then would need to make sure that the version
number is in sync with the version number defined in the :ref:`pyproject` file,
so a better approach is to put the following in your ``__init__.py`` file

.. code-block:: python

    from importlib_metadata import version as _version, PackageNotFoundError
    try:
        __version__ = _version(__name__)
    except PackageNotFoundError:
        pass

This will automatically set ``__version__`` to the global version of the package
declared in :ref:`pyproject` or set by the `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`__ package (see :ref:`setup_py` and
:ref:`pyproject` for more details).

.. _pyproject:

``pyproject.toml``
------------------

The ``pyproject.toml`` file is where we will define the metadata about the package. 
At a minimum, this file should contain the ``[project]`` table (defined by 
`PEP621 <https://peps.python.org/pep-0621/>`_) and the ``[build-system]`` table
(defined by `PEP518 <https://peps.python.org/pep-0518/>`_).

``[project]``
^^^^^^^^^^^^^

.. code-block:: toml

    [project]
    name = "my-package"
    description = "My package description"
    readme = "README.rst"
    authors = [
        { name = "Your Name", email = "your@email.com" }
    ]
    license = { text = "BSD 3-Clause License" }
    dependencies = [
        "numpy",
        "astropy>=3.2",
    ]
    dynamic = ["version"]

    [project.urls]
    homepage = "https://link-to-your-project"

The ``name`` field is the name your package will have on PyPI. It is not necessarily
the same as the module name, so in this case we've set the package name to
``my-package`` even though the module name is ``my_package``. However, aside from
the case where the package name has a hyphen and the module name has an underscore,
we strongly recommend making the package and the module name the same to avoid confusion.

Note that the version of the package is **not** explicitly defined in the file above, 
(rather, defined as ``dynamic``), because we are using the 
`setuptools_scm <https://pypi.org/project/setuptools-scm/>`_ package to automatically 
retrieve the latest version from Git tags. However, if you choose to not use that 
package, you can explicitly set the version in the ``[project]`` section (and remove it
from the ``dynamic`` list):

.. code-block:: toml

    [project]
    version = "0.12"

The ``description`` should be a short one-line sentence that will appear next to your package name
on `PyPI <https://pypi.org>`_ when users search for packages. The ``readme``
defines the ``README.rst`` file, which will be rendered nicely on the PyPI page for the package.

Finally, the ``dependencies`` section is important since it is where you will
be declaring the dependencies for your package. The cleanest way to do this is
to specify one package per line, as shown above. You can optionally include version
restrictions if needed (as shown with ``astropy>=3.2`` above). If your package has no dependencies then you don't need this option.

A complete list of keywords in ``[project]`` can be found in the `Python packaging documentation <https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata>`_.

``[build-system]``
^^^^^^^^^^^^^^^^^^

In the previous section we discussed the ``dependencies`` which can
be used to declare run-time dependencies for the package, which are
dependencies that are needed for the package to import and run correctly.
However, your package may have dependencies that are needed to build the
package in the first place. For example, the :ref:`setup_py` file 
will only run correctly if `setuptools <https://setuptools.readthedocs.io>`_ 
is installed.

The recommended way to specify build-time dependencies is to define the 
``build-system`` table:

.. code-block:: toml

    [build-system]
    requires = ["setuptools", "wheel", "setuptools_scm"]
    build-backend = 'setuptools.build_meta'

If you choose to not use ``setuptools_scm``, you can remove it from this list.
If your package has C extensions that interface with `Numpy <https://numpy.org>`_,
you may also need to add Numpy to the above list - see :ref:`extensions` for
more details.

A complete list of keywords in ``[build-system]`` can be found in `PEP518 <https://packaging.python.org/en/latest/specifications/declaring-build-dependencies/#declaring-build-dependencies>`_.

``[tool.setuptools]``
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    [tool.setuptools]
    zip_safe = false

    [tool.setuptools.packages.find]

The ``zip_safe`` option should be set to ``false`` unless you understand the
implications of setting it to ``true`` - this option is most relevant when
producing application bundles with Python packages.

The ``packages.find`` line can be left as-is - this will automatically determine the
Python modules to install based on the presence of ``__init__.py`` files.

A complete list of keywords in ``[tool.setuptools]`` can be found in the 
`setuptools documentation <https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html>`_.

``[tool.setuptools_scm]``
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: toml

    [tool.setuptools_scm]
    write_to = "my_package/version.py"

The ``[tool.setuptools_scm]`` table indicates that we want to use the `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`_ package to set the version
automatically based on git tags, which will produce version strings such as
``0.13`` for a stable release, or ``0.16.0.dev113+g3d1a8747`` for a developer
version. The ``write_to`` option is not necessary; it will write the parsed version 
to a ``version.py`` with a ``__version__`` variable that can be imported by the 
package itself.

.. _setup_py:

``setup.py``
------------

The ``setup.py`` file used to be where project metadata was defined, before the 
advent of ``setup.cfg`` and then PEP621 and PEP517 (``pyproject.toml``). 
It is no longer necessary to include a ``setup.py`` file in your project, 
unless you are building C extensions in your code.

The minimal ``setup.py`` file is very simple:

.. code-block:: python

    from setuptools import setup
    
    setup()

If you do use ``setuptools_scm``, you have to be aware that **everything** that is git versioned will be included **by default**.
You will have to add::

    prune <folder or files>

to prevent this and slim down your final built package.
This important if you store test files or documentation and do not want to ship them in your final package.

Trying out your package
-----------------------

Once you have committed all of the above files to your repository, you
can test out the package by running

.. code-block:: shell

    pip install .

from the root of the package. Once you have done this, you should be able to
start a Python session from a different directory and type e.g.::

    >>> import my_package
    >>> my_package.__version__
    0.1.dev1+g25976ae

.. TODO: mention about adding more files to package with functionality
