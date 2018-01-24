from abc import ABC, abstractmethod


class IObserver(ABC):
    """
    Abstract interface for observer
    """


    @abstractmethod
    def object_change(self, subject: object) -> None:
        """
        Method which will be called when object changed
        :param subject: target that changed
        """
        pass
