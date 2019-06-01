class LocaleUnsupportedException(Exception):
    """
    Excepción para controlar que el código lingüístico de un país esta soportado
    """

    def __init__(self, message):
        super(LocaleUnsupportedException, self).__init__(message)
