# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import nbmerge

from urllib.request import urlretrieve


# -- Project information -----------------------------------------------------

project = 'ENTR Data Environment'
copyright = '2022, ENTR Alliance'
author = 'ENTR Alliance'

# The full version, including alpha/beta/rc tags
release = '0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "nbsphinx",
    "m2r2"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Copy external documentation files ---------------------------------------

# TODO: Uncomment once Pandoc issue is fixed in github actions
# urlretrieve (
#     "https://raw.githubusercontent.com/entralliance/OpenOA/main/examples/entr/02_plant_aep_analysis_entr.ipynb",
#     "02_plant_aep_analysis.ipynb"
# )

# urlretrieve (
#     "https://raw.githubusercontent.com/entralliance/entr_runtime/dev/README.md",
#     "entr_runtime_readme.md"
# )

urlretrieve (
    "https://raw.githubusercontent.com/entralliance/entr_warehouse/dev/README.md",
    "entr_warehouse_readme.md"
)

# TODO: Uncomment once Pandoc issue is fixed in github actions
# # Merge example Notebooks into one notebook to keep the required structure
# new_nb = nbmerge.merge_notebooks(
#     "./",
#     (
#         "./examples_intro.ipynb",
#         "./02_plant_aep_analysis.ipynb",
#     ),
# )
# nbmerge.write_notebook(new_nb, "./examples_combined.ipynb")