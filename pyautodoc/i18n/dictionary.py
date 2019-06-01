from pyautodoc.i18n.exceptions import LocaleUnsupportedException
from pyautodoc.i18n.locales.es import es
from pyautodoc.i18n.locales.en import en

strings = {'es': es, 'en': en}


class Locale:
    """
    Clase singleton para el control de la internacionalización
    """

    class __Locale:
        """
        Clase privada para la creación del singleton
        """
        def __init__(self, locale):
            """

            :param locale: código del páis
            :type locale: str
            """
            if locale not in strings.keys():
                print(locale)
                raise LocaleUnsupportedException('Unsupported locale')
            self.strings = strings.get(locale)

    instance = None

    def __new__(cls, *args, **kwargs):
        if not Locale.instance:
            Locale.instance = Locale.__Locale(kwargs.get('locale'))
        return Locale.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        return setattr(self.instance, name, value)
