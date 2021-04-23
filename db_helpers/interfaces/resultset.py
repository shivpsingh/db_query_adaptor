from abc import ABC, abstractmethod


class ResultSetInterface(ABC):

    @abstractmethod
    def parse_resultset(self, *args, **kwargs):
        pass
