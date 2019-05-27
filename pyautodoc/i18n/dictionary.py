from pyautodoc.i18n.exceptions import LocaleUnsupportedException
from pyautodoc.i18n.locales import es


strings = {'es':es}


class Locale:

    class __Locale:
        def __init__(self, locale):
            if locale not in strings.keys():
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
