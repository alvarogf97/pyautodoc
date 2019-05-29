import os


def get_abs_path(path, relative_to):
    """
    Obtiene el path absoluto de path si es relativo

    :param str path: ruta
    :param str relative_to: relativa a
    :return: ruta absoluta del path
    :rtype: str
    """
    if not os.path.isabs(path):
        return os.path.abspath(os.path.normpath(os.path.join(relative_to, path)))
    return path
