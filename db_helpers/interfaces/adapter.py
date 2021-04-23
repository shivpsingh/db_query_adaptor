from abc import ABC, abstractmethod


class AdapterInterface(ABC):

    @abstractmethod
    def before_execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute_query(self, *args, **kwargs):
        pass

    @abstractmethod
    def after_execute(self, *args, **kwargs):
        pass
