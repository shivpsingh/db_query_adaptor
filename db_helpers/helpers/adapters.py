from .dispatcher import Dispatcher


class AdaptersDispatcher(Dispatcher):

    NAMESPACE = 'adapters'

    def __init__(self):
        super().__init__(self.NAMESPACE)


Adapters = AdaptersDispatcher()
