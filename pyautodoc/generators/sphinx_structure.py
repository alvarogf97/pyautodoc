import os
from pyautodoc.generators.makefiles import gen_window_makefile, gen_makefile
from pyautodoc.generators.sphinx_config_file import generate_config_file
from pyautodoc.generators.rst_file import generate_index_rst, generate_markdown_rst, \
    generate_package_not_leaf_rst, generate_package_leaf_rst
from pyautodoc.identify.project_structure import identify_structure


def generate_structure(root_folder, project_name, author, version, language_locale, readme_file,
                       license_file, changelog_file):
    """

    :param root_folder:
    :param project_name:
    :param author:
    :param version:
    :param language_locale:
    :param readme_file:
    :param license_file:
    :param changelog_file:
    :return:
    """

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

    root = identify_structure(root_folder)
    modules.extend([mod.filename for mod in root.submodules])

    generate_modules_srt(root)
    generate_index_rst('./source/index.rst', project_name, readme_file, root.python_files, modules)


def generate_modules_srt(root_module):
    """

    :param root_module:
    :return:
    """
    for module in root_module.submodules:
        if module.is_leaf():
            generate_package_leaf_rst('./source/' + module.filename + '.rst', module.name, module.python_files)
        else:
            generate_modules_srt(module)
            generate_package_not_leaf_rst('./source/' + module.filename + '.rst', module.name,
                                          module.python_files, [mod.filename for mod in module.submodules])