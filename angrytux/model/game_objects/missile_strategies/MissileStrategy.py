from abc import ABC, abstractmethod


class MissileStrategy(ABC):
    """
    Interface for missile strategy
    """


    @abstractmethod
    def move(self, missile, gravity: float) -> None:
        """
        Move missile in one tick
        :param missile: Missile object
        :param gravity: actual value of gravity
        """
        pass
