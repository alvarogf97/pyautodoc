class Module:

    def __init__(self, name, python_files, submodules):
        self.name = name
        self.python_files = python_files
        self.submodules = submodules

    def __str__(self):
        return self.name