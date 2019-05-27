import os


def is_package(folder):
    """

    :param folder:
    :return:
    """
    return os.path.isdir(folder) and '__init__.py' in os.listdir(folder)


def get_folder_name(path):
    """

    :param path:
    :return:
    """
    return os.path.basename(os.path.normpath(path))
