import codecs
from pyautodoc.utils.stringify import list_to_rst_modules, generate_headline, generate_sub_headline, get_pyfile_header
from pyautodoc.i18n.dictionary import Locale


def generate_index_rst(file_path, project_name, readme_file_path, python_files, python_packages):
    """

    :param file_path:
    :param project_name:
    :param readme_file_path:
    :param python_files:
    :param python_packages:
    :return:
    """

    readme = ''
    if readme_file_path != '':
        header = Locale().strings.get('getting started')
        readme = header + '\n' + generate_headline(header) + '\n.. mdinclude :: {}'.format(readme_file_path)

    template = """
{}
{}
.. toctree::
   :maxdepth: 3
   :caption: {}
   :name: mastertoc
   
{}
{}

{}
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
    """.format(Locale().strings.get('welcome msg').format(project_name),
               generate_headline(Locale().strings.get('welcome msg').format(project_name)),
               Locale().strings.get('toc'), list_to_rst_modules(python_packages), readme,
               Locale().strings.get('indexes content'))

    includes = ''
    for pyfile in python_files:
        includes = includes + '\n.. automodule:: {}\n   :members:'.format(pyfile)

    template = template + includes
    with codecs.open(file_path, 'w', 'utf-8') as f:
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

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)


def generate_package_leaf_rst(file_path, package_name, python_files):
    """

    :param file_path:
    :param package_name:
    :param python_files:
    :return:
    """
    template = """
{}
{}
   """.format(package_name, generate_headline(package_name))

    for pyfile in python_files:
        template = template + '\n' + get_pyfile_header(pyfile) + '\n' + generate_sub_headline(pyfile) + \
                   '\n.. automodule:: {}\n   :members:'.format(pyfile) + '\n'

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)


def generate_package_not_leaf_rst(file_path, package_name, python_files, python_packages):
    """

    :param file_path:
    :param package_name:
    :param python_files:
    :param python_packages:
    :return:
    """
    template = """
{}
{}
.. toctree::
   :maxdepth: 3
   :caption: {}
   
{}
    """.format(package_name, generate_headline(package_name),
              Locale().strings.get('toc'), list_to_rst_modules(python_packages))

    for pyfile in python_files:
        template = template + '\n' + get_pyfile_header(pyfile) + '\n' + generate_sub_headline(pyfile) + \
                   '\n.. automodule:: {}\n   :members:'.format(pyfile) + '\n'

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)
