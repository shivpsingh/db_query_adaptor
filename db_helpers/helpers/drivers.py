import os
from .dispatcher import Dispatcher


class DriversDispatcher(Dispatcher):

    NAMESPACE = 'drivers'
    LAMBDA_TEMP_DIR = '/tmp'

    def __init__(self):
        super().__init__(self.NAMESPACE)

    def register_for(self, target):
        def wrap(dispatch_class):
            self._registry[self._namespace][
                str(target).lower()
            ] = dispatch_class

            # Create tmp directory for db_configs
            dir_path = os.path.join(
                self.LAMBDA_TEMP_DIR, target
            )

            os.makedirs(dir_path, exist_ok=True)

            return dispatch_class
        return wrap

    def get_for(self, target, params={}):
        try:
            obj = self._registry[self._namespace][
                str(target).lower()
            ]()
            obj.__setattr__(
                'DRIVER_TMP_DIR', os.path.join(
                    self.LAMBDA_TEMP_DIR, str(target).lower()
                )
            )
            for key, val in params.items():
                obj.__setattr__(key, val)

            return obj
        except Exception:
            raise ValueError(
                f"No Driver Found for target {str(target).lower()}"
            )


Drivers = DriversDispatcher()
