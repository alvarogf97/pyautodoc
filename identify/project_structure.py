import os
from identify.packages import is_package, get_folder_name
from templates.rst_file import generate_package_leaf_rst, generate_package_not_leaf_rst


def identify_structure(root_folder, module_name=""):
    """

    :param root_folder:
    :param module_name:
    :return:
    """
    filename = module_name[:-1] if module_name != "" else "Main"
    dirname = get_folder_name(root_folder) if module_name != "" else "Documentation"
    rst_files = []
    python_files = [module_name + os.path.splitext(pyfile)[0] for pyfile in os.listdir(root_folder)
                    if os.path.splitext(pyfile)[1] == '.py' and pyfile != '__init__.py']
    python_packages = [pypackage for pypackage in os.listdir(root_folder) if is_package(root_folder + '/' + pypackage)]

    if len(python_packages) == 0:
        generate_package_leaf_rst('./source/' + filename + '.rst', dirname, python_files)
        rst_files.append(filename + '.rst')
    else:
        for package in python_packages:
            sub_packages = identify_structure(root_folder + '/' + package, module_name + package + '.')
            generate_package_not_leaf_rst('./source/' + filename + '_' + package + '.rst', dirname,
                                          python_files, sub_packages)
            rst_files.append(filename + '_' + package + '.rst')

    return rst_files
