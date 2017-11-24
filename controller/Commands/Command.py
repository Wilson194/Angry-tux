from abc import ABC, abstractmethod


class Command(ABC):
    """
    Command interface
    """


    def __init__(self):
        self.__memento = None


    @property
    def memento(self):
        return self.__memento


    @memento.setter
    def memento(self, memento):
        self.__memento = memento


    @abstractmethod
    def execute(self):
        """
        Execute command (do what command should do)
        :return:
        """
        pass


    @abstractmethod
    def undo(self):
        """
        Undo command (use memento for undo operation)
        :return:
        """
        pass


    @property
    @abstractmethod
    def create_memento(self):
        """
        Property, yes if create a memento, no otherwise
        :return:
        """
        pass
