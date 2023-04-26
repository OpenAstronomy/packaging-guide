.. _data:

Including data in your package
==============================

Using ``setuptools_scm`` to link your Python package to your git repository also makes including data easy.
By setting ``include_package_data = true`` in the ``[tool.setuptools]`` section of ``pyproject.toml``, ``setuptools_scm`` will automatically include all files tracked by git in your package.
While this is useful for including required non-Python files, it's pretty common to have files that don't belong in your distribution in your git repository, such as continuious integration configurations, or even git config files.
It's possible to exclude certain files and directories which are tracked by git from being included in your built package by adding ``exclude`` or ``prune`` lines to the ``MANIFEST.in`` file in the root of the repository.
An example ``MANIFIEST.in`` file might look like::

    # Exclude specific files
    # All files which are tracked by git and not explicitly excluded here are included by setuptools_scm
    # exclude whole directories from the package
    prune .github
    # exclude specific files from the package
    exclude .mailmap
    exclude .gitignore
    exclude .gitattributes
    exclude *.yml
    exclude *.yaml


If you need to explicitly include a file, for example ``important.yaml``, when there is a more generic exclude you need to include that file *after* the more general exclude statement as the commands are processed in order.
See the `Python packaging guide <https://packaging.python.org/guides/using-manifest-in/>`__ for more details.
