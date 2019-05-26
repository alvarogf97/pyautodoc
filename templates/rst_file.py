from utils.stringify import list_to_rst_modules, generate_headline


def generate_index_rst(file_path, project_name, readme_file_path, rst_files):
    """

    :param file_path:
    :param project_name:
    :param readme_file_path:
    :param rst_files:
    :return:
    """

    template = """
Welcome to {}'s documentation!
========================================
.. mdinclude :: {}
.. toctree::
   :maxdepth: 4
   :caption: Table of Contents
   :name: mastertoc

{}

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
    """.format(project_name, readme_file_path, list_to_rst_modules(rst_files))

    with open(file_path, 'w') as f:
        f.write(template)


def generate_markdown_rst(file_path, name, md_file_path):
    """

    :param file_path:
    :param name:
    :param md_file_path:
    :return:
    """

    template = """
{}
{}
.. mdinclude :: {}

    """.format(name, generate_headline(name), md_file_path)

    with open(file_path, 'w') as f:
        f.write(template)


def generate_package_leaf_rst(file_path, package_name, modules):

    template = """
{}
{}
   """.format(package_name, generate_headline(package_name))

    for module in modules:
        template = template + '\n.. automodule:: {}\n   :members:'.format(module)

    with open(file_path, 'w') as f:
        f.write(template)


def generate_package_not_leaf_rst(file_path, package_name, modules, sub_modules):
    template = """
{}
{}
.. toctree::
   :maxdepth: 2
   :caption: Table of Contents
   
{}
   """.format(package_name, generate_headline(package_name), list_to_rst_modules(sub_modules))

    for module in modules:
        template = template + '\n.. automodule:: {}\n   :members:'.format(module)

    with open(file_path, 'w') as f:
        f.write(template)
