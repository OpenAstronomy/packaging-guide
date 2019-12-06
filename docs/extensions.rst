.. _extensions:

Compiled C/Cython extensions
============================

Python packages can include compiled extensions in a variety of languages, most
commonly C and `Cython <https://cython.org/>`_ (Cython is a language close to
Python that can be automatically translated into C). An extension, once
compiled, looks just like a regular Python module/sub-module.

There are a number of reasons why you might want to include compiled extensions
including for example to speed up code that is otherwise slow in Python, or
because you want to include an existing stable library without having to
re-implement it in Python.

Defining extensions in setup.py
-------------------------------

To define an extension, we need to create an instance of
:class:`distutils.core.Extension` inside the ``setup.py`` file. For a simple
case with a single ``.c`` file, this would look like::

    from distutils.core import Extension
    ext = Extension(name='my_package.my_extension',
                    sources=['my_package/my_extension.c'])

Here ``name`` is the final name the compiled extension will have, which means
that if the extension defines a function ``fast_function`` it can be imported
as::

    from my_package.my_extension import fast_function

The ``sources`` argument should be set to a list of source files to compile and
link together to create the extension, and the filenames should be relative to
the ``setup.py`` file. If your extension uses the Numpy C API, you should also
specify the Numpy include directory using::

    ext = Extension(name='my_package.my_extension',
                    sources=['my_package/my_extension.c'],
                    include_dirs=[numpy.get_include()])

There are a number of other options that can be passed to set for example what
other libraries to link to, flags or macros to pass to the compiler, and so on.
For more information about these, see the :class:`Extension section
<distutils.core.Extension>` in the Python documentation.

Once your extension has been defined, you should pass a list of extensions
to the ``ext_modules`` keyword argument to the ``setup()`` function in the
``setup.py`` file::

    setup(..., ext_modules=[ext])

If you want to build a Cython extension instead of a C extension, specify the
``.pyx`` file(s) in the ``sources`` argument::

    ext = Extension(name='my_package.my_extension',
                    sources=['my_package/my_extension.pyx'])

And make sure you also add ``cython`` to your ``pyproject.toml`` build-time
dependencies::

    [build-system]
    requires = [..., "cython"]
    build-backend = 'setuptools.build_meta'

Packages with many extensions
-----------------------------

For packages with many extensions, you might want to consider using the
`extension-helpers <https://pypi.org/project/extension-helpers/>`_ package. This
package serves two main purposes:

* For single-file Cython extensions, it will automatically discover and
  define these extensions.

* For other extensions, it allows you to define extensions inside
  ``setup_package.py`` files which can be anywhere in your package. These files
  should contain a single function called ``get_extensions`` that returns a list
  of extensions. The idea is then to make it easier to manage extensions for
  large packages by placing the ``setup_package.py`` files close to the
  extension code.

To use extension-helpers, first make sure it is included in your ``pyproject.toml``
file as a build-time dependency::

     [build-system]
     requires = [..., "extension-helpers"]
     build-backend = 'setuptools.build_meta'

Then adjust your ``setup.py`` to include::

     from extension_helpers.setup_helpers import get_extensions

     setup(..., ext_modules=get_extensions())

Finally, if needed, create ``setup_package.py`` files in sub-modules where you
have extensions, add a ``get_extensions()`` function, and make sure that it
returns a list of :class:`~distutils.core.Extension`  objects.
