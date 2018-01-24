from abc import ABC, abstractmethod


class EnemyState(ABC):
    """
    Interface for enemy states
    """


    def __init__(self, enemy):
        self._enemy = enemy


    @property
    @abstractmethod
    def delete(self) -> bool:
        """
        Property, if this object should be deleted by garbage collector
        :return:
        """
        pass


    @abstractmethod
    def hit(self) -> None:
        """
        Method for hit this enemy (what to do when hitted)
        """
        pass


    @abstractmethod
    def move(self) -> bool:
        """
        Method for move enemy for one tick
        :return:
        """
        pass


    @property
    @abstractmethod
    def collidable(self) -> bool:
        """
        Property, if this object can collid with missile
        :return:
        """
        pass
