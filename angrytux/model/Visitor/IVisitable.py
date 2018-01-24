from abc import ABC, abstractmethod


class IVisitable(ABC):
    """
    Abstract interface that define visitable object for visitor
    """


    @abstractmethod
    def accept(self, visitor):
        """
        Accept the visitor
        :param visitor: visitor object
        """
        pass
