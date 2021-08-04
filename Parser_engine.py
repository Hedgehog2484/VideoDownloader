from abc import ABC, abstractmethod


class ParserEngine(ABC):

    @abstractmethod
    def check_user_input(self):
        pass


    @abstractmethod
    def parsing(self, path, link):
        pass
