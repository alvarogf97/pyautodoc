class Module:
    """
    Un módulo es un paquete contenedor de python

    .. code-block:: python

        >> print(myModule)
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

    def __init__(self, name, python_files, submodules, filename):
        """

        :param str name: Nombre del módulo python
        :param list[PythonFile] python_files: ficheros ``.py`` dentro del módulo python
        :param list[Module] submodules: submodulos
        :param str filename: nombre del fichero ``.rst`` de salida del módulo
        """

        self.name = name
        self.python_files = python_files
        self.submodules = submodules
        self.filename = filename

    def is_leaf(self):
        """
        Comprueba si el paquete es un paquete sin submódulos

        :return: True si lo es, False en otro caso
        :rtype: bool
        """
        return len(self.submodules) == 0

    def __str__(self, indentation=""):
        schema = '\n' + indentation + '|--' + self.name
        for pyfile in self.python_files:
            schema = schema + '\n' + indentation + '|----' + pyfile.name + '.py'
        for module in self.submodules:
            schema = schema + module.__str__(indentation + "    ")
        return schema


class PythonFile:
    """
    Un PythonFile es la representación de un fichero python,
    que contiene su nombre y las clases que implementa
    """

    def __init__(self, name, classes):
        """

        :param str name: nombre del fichero ``.py``
        :param list[str] classes: clases que implementa el fichero
        """

        self.name = name
        self.classes = []
