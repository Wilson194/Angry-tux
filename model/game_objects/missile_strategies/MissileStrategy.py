from abc import ABC, abstractmethod

from model.game_objects.Position import Position


class MissileStrategy(ABC):
    @abstractmethod
    def move(self, missile, gravity: float):
        pass
