from abc import ABC, abstractmethod


class Command(ABC):
    """
    Command interface
    """


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
