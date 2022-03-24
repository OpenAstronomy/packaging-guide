.. _scripts:

Command-line scripts
====================

The recommended way to add command-line scripts to your package is to make use of the
setuptools ``console_scripts`` entry point, as described in the `setuptools
documentation <https://setuptools.pypa.io/en/latest/userguide/entry_point.html#console-scripts>`_.
If you want to add command-line arguments/flags to your script, we recommend using
`click <https://click.palletsprojects.com>`_ package which makes this much easier.
