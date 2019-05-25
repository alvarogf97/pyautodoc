import os
from templates.makefiles import gen_window_makefile, gen_makefile
from templates.sphinx_config_file import generate_config_file
from templates.rst_file import generate_index_rst


def generate_structure(root_folder, project_name, author, version, language_locale):

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
    generate_index_rst('./source/index.rst')

