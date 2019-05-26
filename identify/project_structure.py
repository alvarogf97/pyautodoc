import os
from identify.packages import is_package
from identify.data import Module


def identify_structure(root_folder, modules_structure=[], name="Root"):
    """

    :param root_folder:
    :param modules_structure:
    :return:
    """
    module_name = '.'.join(modules_structure) + '.' if len(modules_structure) > 0 else ''
    python_files = [module_name + os.path.splitext(pyfile)[0] for pyfile in os.listdir(root_folder)
                    if os.path.splitext(pyfile)[1] == '.py' and pyfile != '__init__.py']
    python_packages = [pypackage for pypackage in os.listdir(root_folder) if is_package(root_folder + '/' + pypackage)]

    submodules = []
    for package in python_packages:
        modules_structure.append(package)
        submodules.append(identify_structure(os.path.join(root_folder, package), modules_structure, package))
        modules_structure.remove(package)

    return Module(name, python_files, submodules)
