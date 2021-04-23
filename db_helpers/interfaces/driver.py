from abc import ABC, abstractmethod


class DriverInterface(ABC):

    @abstractmethod
    def init_db_settings(self, *args, **kwargs):
        pass

    @abstractmethod
    def test_connection(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_db_instance(self, *args, **kwargs):
        pass
