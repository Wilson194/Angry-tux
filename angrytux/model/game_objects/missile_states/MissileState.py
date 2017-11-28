from abc import ABC, abstractmethod


class MissileState(ABC):
    """
    Interface for missile state
    """


    @property
    @abstractmethod
    def delete(self):
        """
        Property which determinate, if this object should be deleted by garbage collector
        :return:
        """
        pass
