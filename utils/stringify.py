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