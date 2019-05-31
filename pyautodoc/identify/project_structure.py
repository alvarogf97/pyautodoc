import os
import ast
from pyautodoc.identify.packages import is_package
from pyautodoc.identify.data import Module, PythonFile


def identify_structure(root_folder, excludes, ignores, modules_structure=None, name="Root"):
    """

    :param root_folder:
    :param excludes:
    :param ignores:
    :param modules_structure:
    :param name:
    :return:
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

    :param pyfile_path:
    :return:
    """
    with open(pyfile_path, 'r') as f:
        inspection = ast.parse(f.read())

    return [class_.name for class_ in inspection.body if isinstance(class_, ast.ClassDef)]
