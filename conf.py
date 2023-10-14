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
# import nbmerge
import os
from datetime import datetime
from urllib.request import urlretrieve
from dotenv import load_dotenv

load_dotenv()

# default "dev" external repos/branches
default_branch = os.getenv("DEFAULT_GITBRANCH") or 'main'
OPENOA_GITREPO = os.getenv("OPENOA_GITREPO") or 'entralliance/OpenOA'
OPENOA_GITBRANCH = os.getenv("OPENOA_GITBRANCH") or default_branch
ENTR_RUNTIME_GITBRANCH = os.getenv("ENTR_RUNTIME_GITBRANCH") or default_branch
ENTR_WAREHOUSE_GITBRANCH = os.getenv("ENTR_WAREHOUSE_GITBRANCH") or default_branch
DBT_ENTR_GITBRANCH = os.getenv("DBT_ENTR_GITBRANCH") or default_branch
DBT_OPENOA_GITBRANCH = os.getenv("DBT_OPENOA_GITBRANCH") or default_branch

# -- Project information -----------------------------------------------------

project = 'ENTR'
copyright = f'{datetime.today().strftime("%Y")}, ENTR Foundation'
author = 'ENTR Foundation'

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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_external', 'content', 'archive', 'Readme.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        # "relations.html",
        "searchbox.html",
        # "donate.html",
    ]
}
html_theme_options = {
    "description": "Open data standards for clean energy",
    "github_user": "entralliance",
    "github_repo": "entralliance.github.io",
    "github_button": True,
    "github_type": "follow",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Copy external documentation files ---------------------------------------

# TODO: Uncomment once Pandoc issue is fixed in github actions
# urlretrieve (
#     f"https://raw.githubusercontent.com/{OPENOA_GITREPO}/{OPENOA_GITBRANCH}/examples/entr/02_plant_aep_analysis_entr.ipynb",
#     "_external/02_plant_aep_analysis.ipynb"
# )

# urlretrieve (
#     f"https://raw.githubusercontent.com/entralliance/entr_runtime/{ENTR_RUNTIME_GITBRANCH}/README.md",
#     "_external/entr_runtime_readme.md"
# )


urlretrieve (
    f"https://raw.githubusercontent.com/entralliance/dbt-entr/{DBT_ENTR_GITBRANCH}/README.md",
    "_external/dbt-entr-readme.md"
)

urlretrieve (
    f"https://raw.githubusercontent.com/entralliance/dbt-openoa/{DBT_OPENOA_GITBRANCH}/README.md",
    "_external/dbt-openoa-readme.md"
)

urlretrieve (
    f"https://raw.githubusercontent.com/entralliance/entr_warehouse/{ENTR_WAREHOUSE_GITBRANCH}/README.md",
    "_external/entr_warehouse_readme.md"
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
