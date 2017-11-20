from abc import ABC, abstractmethod

from model.game_objects.Position import Position


class MissileStrategy(ABC):
    @abstractmethod
    def move(self, gravity: float, position: Position, movement_angle: float, speed: float):
        pass
