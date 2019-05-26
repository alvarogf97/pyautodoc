def list_to_rst_modules(list_):
    """

    :param list_:
    :return:
    """

    result = ""
    for element in list_:
        result = result + "   " + element + "\n"
    return result


def generate_headline(text):
    """

    :param text:
    :return:
    """
    return "=" * (len(text) + 4)


def generate_sub_headline(text):
    """

    :param text:
    :return:
    """
    return "#" * (len(text) + 4)


def get_pyfile_header(pyfile):
    """

    :param pyfile:
    :return:
    """
    return pyfile.split('.')[-1]


def convert_path(path):
    """

    :param path:
    :return:
    """
    return path.replace('\\','\\\\')