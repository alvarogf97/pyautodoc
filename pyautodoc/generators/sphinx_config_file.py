import datetime


def generate_config_file(root_folder, project_name, author, version, language_locale, file_path):
    """
    Generate python configuration file with needed information

    :param root_folder:
    :param project_name:
    :param author:
    :param version:
    :param language_locale:
    :param file_path:
    :return:
    """

    template = """
# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('{}'))


# -- Project information -----------------------------------------------------

project = '{}'
copyright = '{}'
author = '{}'

# The full version, including alpha/beta/rc tags
release = '{}'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary', 'm2r']
source_suffix = ['.rst', '.md']
# NOTE: Don't overwrite your old extension list! Just add to it!

autodoc_default_flags = ['members']
autosummary_generate = True

# Add any paths that contain generators here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = '{}'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static'] 
""".format(root_folder, project_name, str(datetime.datetime.now().year) + ', ' + author, author, version,
           language_locale)

    with open(file_path, 'w') as f:
        f.write(template)