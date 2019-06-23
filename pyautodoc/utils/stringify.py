def list_to_rst_modules(list_):
    """
    Combina los nombres de los módulos para formatearlos
    e incluirlos en un fichero ``.rst``

    :param list[str] list_: lista con los nombres de los módulos
    :return: string formateada para ``.rst``
    :rtype: str

    .. code-block:: python

        >> list_to_rst_modules(['generators', 'identify', 'utils'])
        "generators \\n identify \\n utils"

    """

    result = ""
    for element in list_:
        result = result + "   " + element + "\n"
    return result


def generate_headline(text):
    """
    Genera la cabecer para los titulos formateados en ``.rst``

    :param str text: texto para el que generar la cabecera
    :return: cabecera para el texto
    :rtype: str

    .. code-block:: python

        >> generate_headline('Welcome')
        '==========='

    """
    return "=" * (len(text) + 6)


def generate_sub_headline(text):
    """
    Genera la cabecer para los subtitulos formateados en ``.rst``

    :param str text: texto para el que generar la cabecera
    :return: cabecera para el texto
    :rtype: str

    .. code-block:: python

        >> generate_sub_headline('Welcome')
        '###########'

    """
    return "#" * (len(text) + 6)


def generate_sub_sub_headline(text):
    """
    Genera la cabecer para los subsubtitulos formateados en ``.rst``

    :param str text: texto para el que generar la cabecera
    :return: cabecera para el texto
    :rtype: str

    .. code-block:: python

        >> generate_sub_sub_headline('Welcome')
        '***********'

    """
    return "*" * (len(text) + 6)


def get_pyfile_header(pyfile):
    """
    Obtiene el nombre del fichero

    :param str pyfile: nombre completo de la ruta del fichero ``.py``
    :return: nombre del fichero
    :rtype: str

    .. code-block:: python

        >> get_pyfile_header('../a/c.py')
        'c'

    """
    return pyfile.split('.')[-1]


def convert_path(path):
    """
    Escapa la ruta pasada por parámetros

    :param str path: ruta
    :return: ruta escapada
    :rtype: str

    .. code-block:: python

        >> convert_path('..\a\c.py')
        '..\\a\\c.py'

    """
    return path.replace('\\', '\\\\')


def generate_mocks_stuff(mocks_list):
    """
    Convierte una lista a string

    :param mocks_list: lista de las importaciones que no deben realizarse
    :return: lista en formato string
    :rtype: str

    .. code-block:: python

        >> convert_path(['a', 'b'])
        '['a', 'b']'

    """
    if len(mocks_list) == 0:
        return '[]'
    else:
        string_list = '['
        for mock in mocks_list:
            string_list = string_list + '\"' + mock + '\", '
        string_list = string_list[:-2] + ']'
        return string_list
