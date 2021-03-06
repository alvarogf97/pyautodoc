
# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('C:\\Users\\alvaro\\pyautodoc\\pyautodoc'))


# -- Project information -----------------------------------------------------

project = 'PyAutoDoc'
copyright = '2019, Alvaro'
author = 'Alvaro'

# The full version, including alpha/beta/rc tags
release = '0.6'

master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo', 'sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'm2r']
extensions.extend(["sphinx.ext.githubpages"])
source_suffix = ['.rst', '.md']
# NOTE: Don't overwrite your old extension list! Just add to it!

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '',
    'undoc-members': False,
    'exclude-members': ''
}
autodoc_mock_imports = ["django", "pyautodoc"]
autoclass_content = 'both'
autosummary_generate = True

# Add any paths that contain generators here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'alabaster'
html_theme_options = {'logo': 'logo.png', 'github_user': 'alvarogf97', 'github_repo': 'pyautodoc', 'fixed_sidebar': True, 'description': '¡Automatiza la documentación de tu proyecto!'}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
latex_engine = 'pdflatex'
latex_logo = 'C:\\Users\\alvaro\\Desktop\\alvaro\\cosillas\\w.jpg'
