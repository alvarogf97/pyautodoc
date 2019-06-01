import os
from pyautodoc.i18n.dictionary import Locale
from pyautodoc.generators.makefiles import gen_window_makefile, gen_makefile
from pyautodoc.generators.sphinx_config_file import generate_config_file
from pyautodoc.generators.rst_file import generate_index_rst, generate_markdown_rst, \
    generate_package_not_leaf_rst, generate_package_leaf_rst
from pyautodoc.identify.project_structure import identify_structure


def generate_structure(root_folder, project_name, author, version, language_locale, readme_file,
                       license_file, changelog_file, excludes=None, ignores=None, html_options=None,
                       latex_options=None, mocks_imports=None, sphinx_extensions=None):
    """
    Genera la estructura de Sphinx de acuerdo a los parámetros recibidos.

    :param str root_folder: ruta de la carpeta raíz del proyecto a documentar
    :param str project_name: nombre del proyecto
    :param str author: autor
    :param str version: versión
    :param str language_locale: código lingüístico del país
    :param str readme_file: ruta del fichero ``README.md``
    :param str license_file: ruta del fichero ``LICENSE.md``
    :param str changelog_file: ruta del fichero ``CHANGELOG.md``
    :param list excludes: lista con los elementos a excluir
    :param list ignores: lista con los elementos a ignorar
    :param dict html_options: diccionario con la configuración html de Sphinx
    :param dict latex_options: diccionario con la configuración LaTeX de Sphinx
    :param list mocks_imports: lista con las importaciones que deben ignorarse dentro del proyecto
    """

    if excludes is None:
        excludes = []
    if ignores is None:
        ignores = []

    Locale(locale=language_locale)
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

    generate_config_file(root_folder=root_folder, project_name=project_name, author=author, version=version,
                         language_locale=language_locale, file_path='./source/conf.py', html_options=html_options,
                         latex_options=latex_options, mocks_imports=mocks_imports, extra_extensions=sphinx_extensions)
    modules = []

    if changelog_file != "":
        generate_markdown_rst('./source/changelog.rst', 'Changelog', changelog_file)
        modules.append('changelog')

    if license_file != "":
        generate_markdown_rst('./source/license.rst', 'License', license_file)
        modules.append('license')

    root = identify_structure(root_folder, excludes, ignores)
    modules.extend([mod.filename for mod in root.submodules])

    generate_modules_srt(root)
    generate_index_rst('./source/index.rst', project_name, readme_file, root.python_files, modules)


def generate_modules_srt(root_module):
    """
    Genera los ficheros ``.rst`` de los módulos identificados

    :param Module root_module: módulo raíz del proyecto a documentar
    """
    for module in root_module.submodules:
        if module.is_leaf():
            generate_package_leaf_rst('./source/' + module.filename + '.rst', module.name, module.python_files,
                                      module.init_file)
        else:
            generate_modules_srt(module)
            generate_package_not_leaf_rst('./source/' + module.filename + '.rst', module.name,
                                          module.python_files, [mod.filename for mod in module.submodules],
                                          module.init_file)
