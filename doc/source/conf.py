# -*- coding: utf-8 -*-
#
# openstackdocstheme documentation build configuration file

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import os
import sys

sys.path.append(os.path.abspath("./_ext"))

extensions = [
    'sphinx.ext.intersphinx',
    'otcdocstheme',
    'cont'
]

# openstackdocstheme options
otcdocs_repo_name = 'opentelekomcloud-infra/docsportal'

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
copyright = u'2017-2021, OpenTelekomCloud Contributors'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'otcdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
otcdocs_auto_version = False

html_favicon = '_static/favicon.ico'

# To use the API Reference sidebar dropdown menu,
# uncomment the html_theme_options parameter.  The theme
# variable, sidebar_dropdown, should be set to `api_ref`.
# Otherwise, the list of links for the User and Ops docs
# appear in the sidebar dropdown menu.
html_theme_options = {
    'show_other_versions': False,
    'sidebar_mode': 'toctree',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/default.css'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

templates_path = ['templates']

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'os-doc-demo.tex', u'os-doc-demo Documentation',
   u'OpenTelekomCloud Contributors', 'manual'),
]

# -- Intersphinx
intersphinx_mapping = {
#    'otce': ('https://docs.otc-service.com/python-otcextensions', None)
}
