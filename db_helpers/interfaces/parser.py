from abc import ABC, abstractmethod


class ParserInterface(ABC):

    @abstractmethod
    def parse_query(self, *args, **kwargs):
        pass
