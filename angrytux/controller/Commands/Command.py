from abc import ABC, abstractmethod


class Command(ABC):
    """
    Command interface
    """


    def __init__(self):
        self.__memento = None


    @property
    def memento(self) -> object:
        """
        Memento object getter
        """
        return self.__memento


    @memento.setter
    def memento(self, memento):
        """
        Setter for memento save
        :param memento: memento object
        """
        self.__memento = memento


    @abstractmethod
    def execute(self):
        """
        Execute command (do what command should do)
        """
        pass


    @abstractmethod
    def undo(self):
        """
        Undo command (use memento or just operatio for undo operation)
        """
        pass


    @property
    @abstractmethod
    def create_memento(self) -> bool:
        """
        Property for determinate, if create memento
        True -> create memento after command
        False -> don't create memento after command
        :return: True/False
        """
        pass
