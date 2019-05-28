class Module:

    def __init__(self, name, python_files, submodules, filename):
        """

        :param name:
        :param python_files:
        :param submodules:
        :param filename:
        """

        self.name = name
        self.python_files = python_files
        self.submodules = submodules
        self.filename = filename

    def is_leaf(self):
        """

        :return:
        """
        return len(self.submodules) == 0

    def __str__(self, indentation=""):
        """
        
        :param indentation:
        :return:
        """
        schema = '\n' + indentation + '|--' + self.name
        for pyfile in self.python_files:
            schema = schema + '\n' + indentation + '|----' + pyfile.name + '.py'
        for module in self.submodules:
            schema = schema + module.__str__(indentation + "    ")
        return schema


class PythonFile:

    def __init__(self, name, classes):
        """

        :param name:
        :param classes:
        """

        self.name = name
        self.classes = classes
