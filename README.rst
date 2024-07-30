SunPy Package Template
======================

This repo extends the `OpenAstronomy Python Packaging Guide <https://packaging-guide.openastronomy.org/en/latest/>`__ to add SunPy specific features such as config files which are shared over all of SunPy's packages.

Previewing Rendered Templates
-----------------------------

To make it easier to preview changes to files when rendering the template there is a tox environment named ``bake_cookies``.
If you run ``tox -e bake_cookies`` a new directory named ``cookies`` will be present with a variety of test renders of the template in (see ``tests/conftest.py`` for the configuration options).
