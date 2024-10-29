# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import datetime

from packaging.version import Version

# -- Project information -----------------------------------------------------

# The full version, including alpha/beta/rc tags
from {{ cookiecutter.module_name }} import __version__

_version = Version(__version__)
version = release = str(_version)
# Avoid "post" appearing in version string in rendered docs
if _version.is_postrelease:
    version = release = _version.base_version
# Avoid long githashes in rendered Sphinx docs
elif _version.is_devrelease:
    version = release = f"{_version.base_version}.dev{_version.dev}"
is_development = _version.is_devrelease
is_release = not(_version.is_prerelease or _version.is_devrelease)

project = "{{ cookiecutter.package_name }}"
author = "{{ cookiecutter.author_name }}"
copyright = f"{datetime.datetime.now().year}, {author}"  # noqa: A001

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# Treat everything in single ` as a Python reference.
default_role = "py:obj"

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"python": ("https://docs.python.org/", None)}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "{{ cookiecutter._sphinx_theme }}"

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    "-Nfontsize=10",
    "-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Efontsize=10",
    "-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Gfontsize=10",
    "-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# By default, when rendering docstrings for classes, sphinx.ext.autodoc will
# make docs with the class-level docstring and the class-method docstrings,
# but not the __init__ docstring, which often contains the parameters to
# class constructors across the scientific Python ecosystem. The option below
# will append the __init__ docstring to the class-level docstring when rendering
# the docs. For more options, see:
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autoclass_content
autoclass_content = "both"

# -- Other options ----------------------------------------------------------
