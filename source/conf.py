# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'uHandPi'
copyright = '2024, Hiwonder'
author = 'Hiwonder'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_markdown_tables','myst_parser','sphinx.ext.intersphinx','sphinx_copybutton']

templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = [
    "attrs_block",
    "colon_fence",
    "substitution",
]

intersphinx_mapping = {
    "myproject": ("https://docs.hiwonder.com/projects/TurboPi/en/latest/", "objects.inv"),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['style.css']