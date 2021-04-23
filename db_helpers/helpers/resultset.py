from .dispatcher import Dispatcher


class ResultSetDispatcher(Dispatcher):

    NAMESPACE = 'resultset'

    def __init__(self):
        super().__init__(self.NAMESPACE)


ResultSet = ResultSetDispatcher()
