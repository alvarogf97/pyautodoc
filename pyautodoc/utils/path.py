import os


def get_abs_path(path, relative_to):
    if not os.path.isabs(path):
        return os.path.abspath(os.path.normpath(os.path.join(relative_to, path)))
    return path
