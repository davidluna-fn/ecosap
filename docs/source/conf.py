# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(1, os.path.abspath('../../'))

project = 'EcoSAP'
copyright = '2023, David Luna'
author = 'David Luna'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # Core Sphinx library for auto html doc generation from docstrings
    'sphinx.ext.autosummary',  # Create neat summary tables for modules/classes/methods etc
    # Link to other project's documentation (see mapping below)
    'sphinx.ext.intersphinx',
    # Add a link to the Python source code for classes, functions etc.
    'sphinx.ext.viewcode',
    # Automatically document param types (less noise in class signature)
    'sphinx_autodoc_typehints',
    'sphinx.ext.githubpages',
    #    'sphinx.ext.napoleon',
    'sphinx.ext.autosectionlabel',
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
