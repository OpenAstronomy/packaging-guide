.. _releasing:

Releasing Your Package
======================

In this section we will describe how to take your package and publish a release to PyPI.

There are a lot of permutations on how to release your package, and depending on
the size of your project you may need to build on this guide. The objective of
this is to provide you with the basic information you need to release something
built by following the rest of this guide.

This section of the guide is assuming you configured `setuptools_scm
<https://pypi.org/project/setuptools-scm/>`__ in the :ref:`minimal` guide. If
you didn't you will need to update your ``setup.cfg`` file as well as using
``git tag``.

Incrementing Version Numbers
----------------------------

When you are ready to release your package you need to give it a version number.
A version number for a release should generally be of the form ``X.Y.Z``, for
full details on versioning Python packages see `PEP 440
<https://www.python.org/dev/peps/pep-0440/>`__. What meaning is conveyed by the
version numbers is up to you, there are multiple different thoughts on this, for
some examples see `Astropy
<https://github.com/astropy/astropy-APEs/blob/master/APE2.rst>`__, `SunPy
<https://github.com/sunpy/sunpy-SEP/blob/master/SEP-0009.md>`__ or `Semantic
Versioning <https://semver.org/>`__.

In this example we are going to release version ``0.1.0`` of our package
``my_package``. When doing releases it is common practice to use `git tags
<https://git-scm.com/book/en/v2/Git-Basics-Tagging>`__ to identify the commit
the release relates to in the history. By using ``setuptools_scm`` these tags
become the reference for the version numbers of your Python package. This means
you only have to increment your version number using git.

To mark a new release of your package in your git history run:

.. code-block:: console

   $ git tag -a v0.1.0 -m "Release version 0.1.0"

Here we use the convention of prepending release tags with ``v``.

If you now import your package and print ``my_package.__version__`` it should say
``0.1.0``.


Building Source Distributions
-----------------------------

Now you have tagged your release, you need to build what is called a "source
distribution" to upload to `PyPI <https://pypi.org/>`__ or the Python Package
Index. This is the place where tools like ``pip`` download packages from and is
the primary place people will search for installable Python packages.

The source distribution is a tarball of all the files needed by your package,
which includes everything in your ``my_package`` directory as well as everything
specified in your :ref:`manifest` file.

The most common way to build a source distribution (sdist) is with ``python
setup.py sdist``. This will put a tarball in the ``dist/`` folder next to your
``setup.py`` file. As we have setup a package with a :ref:`pyproject` file, we
recommend you use the `build <https://pypa-build.readthedocs.io/en/latest/>`__ package to
build your sdist in the isolated environment specified in :ref:`pyproject`. You can do this with:

.. code-block:: console

   $ pip install build
   $ python -m build --sdist --outdir dist .

This is equivalent to running ``python setup.py sdist`` but ensures that the
state of your local environment does not affect the generated package.

Publishing to PyPI
------------------

Now you have created the sdist to be uploaded to PyPI you can upload it with the
`twine <https://pypi.org/project/twine/>`__ package:

.. code-block:: console

   $ pip install twine
   $ twine upload dist/my_package*.tar.gz

This should ask you for your PyPI account details, and will create your project
on PyPI if it doesn't already exist.

Releasing from Branches
-----------------------

If your project is larger, you might want to create branches for each of your
major release versions to make it easy to continue to support those releases
with bug fixes while continuing development of your master branch.

If you follow this pattern for your releases you will have to perform one extra
step when using ``setuptools_scm``, which is to also increment the version with
a tag on the master branch to indicate you have started to develop a new version
on your master branch. To do this at the point where you branch for your
upcoming release push a tag for ``vX.Ydev`` where ``X.Y`` is the version number
of the next major release e.g. if you just branched for 1.1 you would create a
``v1.2dev`` tag.
