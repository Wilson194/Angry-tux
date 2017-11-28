from abc import ABC, abstractmethod


class MissileStrategy(ABC):
    """
    Interface for missile strategy
    """


    @abstractmethod
    def move(self, missile, gravity: float):
        """
        Move missile in one tick
        :param missile:
        :param gravity:
        :return:
        """
        pass
