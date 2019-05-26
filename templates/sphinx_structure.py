import os
from templates.makefiles import gen_window_makefile, gen_makefile
from templates.sphinx_config_file import generate_config_file
from templates.rst_file import generate_index_rst, generate_markdown_rst
from identify.project_structure import identify_structure


def generate_structure(root_folder, project_name, author, version, language_locale, readme_file,
                       license_file, changelog_file):

    if not os.path.isdir('./build'):
        os.mkdir('./build')
    if not os.path.isdir('./source'):
        os.mkdir('./source')

    #  generate makefiles
    gen_window_makefile('./make.bat')
    gen_makefile('./Makefile')

    #  generate source build
    if not os.path.isdir('./source/_static'):
        os.mkdir('./source/_static')
    if not os.path.isdir('./source/_templates'):
        os.mkdir('./source/_templates')

    generate_config_file(root_folder, project_name, author, version, language_locale, './source/conf.py')
    modules = []

    if changelog_file != "":
        generate_markdown_rst('./source/changelog.rst', 'Changelog', changelog_file)
        modules.append('changelog')

    if license_file != "":
        generate_markdown_rst('./source/license.rst', 'License', license_file)
        modules.append('license')

    modules.extend(identify_structure(root_folder))
    generate_index_rst('./source/index.rst', project_name, readme_file, modules)
