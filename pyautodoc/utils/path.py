import os
import ntpath


def get_abs_path(path, relative_to):
    """
    Obtiene el path absoluto de path si es relativo

    :param str path: ruta
    :param str relative_to: relativa a
    :return: ruta absoluta del path
    :rtype: str

    .. code-block:: python

        >> get_abs_path('../c.py', '../dir', 'C:\\<username>\\c.py')
        'c.py'

    """
    if not os.path.isabs(path):
        return os.path.abspath(os.path.normpath(os.path.join(relative_to, path)))
    return path


def path_leaf(path):
    """
    Obtiene el nombre del fichero desde la ruta absoluta

    :param str path: ruta absoluta del fichero
    :return: nombre del fichero
    :rtype: str

    .. code-block:: python

        >> path_leaf('a/b/c.py')
        'c.py'

    """
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
