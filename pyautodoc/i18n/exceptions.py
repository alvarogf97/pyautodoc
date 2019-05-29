class LocaleUnsupportedException(Exception):

    def __init__(self, message):
        super(LocaleUnsupportedException, self).__init__(message)
