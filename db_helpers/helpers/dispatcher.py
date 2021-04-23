class Dispatcher(object):

    _registry = {}

    def __init__(self, namespace):
        namespace = str(namespace).lower()
        if not Dispatcher._registry.get(namespace):
            Dispatcher._registry[namespace] = {}
        self._namespace = namespace

    def register_for(self, target):
        def wrap(dispatch_class):
            self._registry[self._namespace][
                str(target).lower()
            ] = dispatch_class
            return dispatch_class
        return wrap

    def get_for(self, target, params={}):
        try:
            obj = self._registry[self._namespace][str(target).lower()]()
            for key, val in params.items():
                obj.__setattr__(key, val)

            return obj
        except Exception:
            raise ValueError(
                f"No Dispatcher Found for target {str(target).lower()}"
            )
