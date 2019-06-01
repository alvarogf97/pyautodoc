import os
import ast
from pyautodoc.identify.packages import is_package
from pyautodoc.identify.data import Module, PythonFile


def identify_structure(root_folder, excludes, ignores, modules_structure=None, name="Root"):
    """
    Identifica la estructura del proyecto a documentar

    :param str root_folder: carpeta raíz
    :param list excludes: lista de elementos a excluir
    :param list ignores: lista de elementos a ignorar
    :param list modules_structure: lista de los módulos ya recorridos
    :param str name: nombre del nodo
    :return: devuelve el módulo raíz **root** con todos sus submódulos
    :rtype: Module

    .. code-block:: python

        >> identify_structure('../myfolder/pydoc')
        |--Root
            |--generators
                |----generators.makefiles.py
                |----generators.rst_file.py
                |----generators.sphinx_config_file.py
                |----generators.sphinx_structure.py
            |--i18n
                |----i18n.dictionary.py
                |--locales
                    |----i18n.locales.es.py
            |--identify
                |----identify.data.py
                |----identify.packages.py
                |----identify.project_structure.py
            |--utils
                |----utils.path.py
                |----utils.stringify.py

    """

    if modules_structure is None:
        modules_structure = []

    module_name = '.'.join(modules_structure) + '.' if len(modules_structure) > 0 else ''
    python_files = [PythonFile(module_name + os.path.splitext(pyfile)[0],
                               get_classes(os.path.join(root_folder, pyfile))) for pyfile in os.listdir(root_folder)
                    if os.path.splitext(pyfile)[1] == '.py' and pyfile != '__init__.py' and pyfile not in ignores
                    and module_name + pyfile not in excludes]
    python_packages = [pypackage for pypackage in os.listdir(root_folder) if is_package(root_folder + '/' + pypackage)
                       and pypackage not in ignores and '.'.join(modules_structure + [pypackage]) not in excludes]

    submodules = []
    for package in python_packages:
        modules_structure.append(package)
        submodules.append(identify_structure(os.path.join(root_folder, package), excludes, ignores, modules_structure,
                                             package))
        modules_structure.remove(package)

    return Module(name, python_files, submodules, '.'.join(modules_structure))


def get_classes(pyfile_path):
    """
    Obtiene las clases que están dentro de un fichero python

    :param str pyfile_path: nombre del fichero a inspeccionar
    :return: devuelve una lista con todas las clases dentro de un fichero python
    :rtype: list

    .. code-block:: python

        >> get_classes('./data.py')
        ['Module', 'PythonFile']

    """
    with open(pyfile_path, 'r') as f:
        inspection = ast.parse(f.read())

    return [class_.name for class_ in inspection.body if isinstance(class_, ast.ClassDef)]
