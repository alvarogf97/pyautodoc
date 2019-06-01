import os


def is_package(folder):
    """
    Comprueba si una carpeta es un paquete python

    :param str folder: ruta de la carpeta
    :return: True si es un paquete, False en otro caso
    :rtype: bool

    .. code-block:: python

        >> is_package('../pydoc')
        'True'

    """
    return os.path.isdir(folder) and '__init__.py' in os.listdir(folder)


def get_folder_name(path):
    """
    Obtiene el nombra de la carpeta de la ruta especificada

    :param str path: ruta
    :return: nombre de la carpeta de la ruta
    :rtype: str

    .. code-block:: python

        >> get_folder_name('../myfolder/pydoc')
        'pydoc'

    """
    return os.path.basename(os.path.normpath(path))
