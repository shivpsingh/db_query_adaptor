from .dispatcher import Dispatcher


class ParsersDispatcher(Dispatcher):

    NAMESPACE = 'parsers'

    def __init__(self):
        super().__init__(self.NAMESPACE)


Parsers = ParsersDispatcher()
