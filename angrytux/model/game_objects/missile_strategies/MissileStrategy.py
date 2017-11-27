from abc import ABC, abstractmethod


class MissileStrategy(ABC):
    @abstractmethod
    def move(self, missile, gravity: float):
        pass
