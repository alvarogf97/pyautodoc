import codecs
from pyautodoc.utils.stringify import list_to_rst_modules, generate_headline, generate_sub_headline, get_pyfile_header
from pyautodoc.i18n.dictionary import Locale


def generate_index_rst(file_path, project_name, readme_file_path, python_files, python_packages):
    """
    Genera el fichero ``index.rst``, el fichero raíz de la documentación

    :param str file_path: ruta para guardar el fichero
    :param str project_name: nombre del proyecto
    :param str readme_file_path: ruta del fichero README.md
    :param list python_files: lista de los ficheros ``.py`` que deben estar en el fichero
    :param list python_packages: lista de los módulos que deben estar en el fichero
    """

    readme = ''
    if readme_file_path != '':
        readme = '.. mdinclude :: {}'.format(readme_file_path)

    template = """
{}
{}
.. toctree::
   :hidden:
   :maxdepth: 2
   
{}
{}

{}
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
    """.format(Locale().strings.get('welcome msg').format(project_name),
               generate_headline(Locale().strings.get('welcome msg').format(project_name)),
               list_to_rst_modules(python_packages), readme,
               Locale().strings.get('indexes content'))

    includes = ''
    for pyfile in python_files:
        includes = includes + '\n.. automodule:: {}\n   :members:'.format(pyfile.name)

    template = template + includes
    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)


def generate_markdown_rst(file_path, name, md_file_path):
    """
    Genera un fichero ``.rst`` a raíz de uno ``.md`` usando la directiva ```..mdinclude:: `` del
    paquete m2r

    :param str file_path: ruta para guardar el fichero
    :param str name: nombre del fichero markdown
    :param str md_file_path: ruta del fichero markdown
    """

    template = """
{}
{}
.. mdinclude :: {}

    """.format(name, generate_headline(name), md_file_path)

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)


def generate_package_leaf_rst(file_path, package_name, python_files, init):
    """
    Genera el fichero ``.rst`` de un paquete python que no contiene ningún submódulo

    :param str file_path: ruta del fichero para guardar
    :param str package_name: nombre del módulo
    :param list python_files: lista con los fichero ```.py`` del módulo
    :param str init: ruta del fichero ``__init__.py``
    """
    template = """
{}
{}
   """.format(package_name, generate_headline(package_name))

    template = template + '\n.. automodule:: {}\n   :members:'.format(init) + '\n'

    for pyfile in python_files:
        template = template + '\n' + get_pyfile_header(pyfile.name) + '\n' + generate_sub_headline(pyfile.name) + \
                   '\n.. automodule:: {}\n   :members:'.format(pyfile.name) + '\n '
        for class_ in pyfile.classes:
            template = template + '\n.. autoclass:: {}\n   :members:'.format(class_) + '\n'

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)


def generate_package_not_leaf_rst(file_path, package_name, python_files, python_packages, init):
    """
    Genera el fichero ``.rst`` de un paquete python que contiene algún submódulo

    :param str file_path: ruta del fichero para guardar
    :param str package_name: nombre del módulo
    :param list python_files: lista con los fichero ```.py`` del módulo
    :param list python_packages: lista con los submódulos del módulo python
    :param str init: ruta del fichero ``__init__.py``
    """
    template = """
{}
{}

{}
{}
.. toctree::
   :maxdepth: 1
   
{}
    """.format(package_name, generate_headline(package_name), Locale().strings.get('toc'),
               generate_sub_headline(Locale().strings.get('toc')), list_to_rst_modules(python_packages))

    template = template + '\n.. automodule:: {}\n   :members:'.format(init) + '\n'

    for pyfile in python_files:
        template = template + '\n' + get_pyfile_header(pyfile.name) + '\n' + generate_sub_headline(pyfile.name) + \
                   '\n.. automodule:: {}\n   :members:'.format(pyfile.name) + '\n'
        for class_ in pyfile.classes:
            template = template + '\n.. autoclass:: {}\n   :members:'.format(class_) + '\n'

    with codecs.open(file_path, 'w', 'utf-8') as f:
        f.write(template)
