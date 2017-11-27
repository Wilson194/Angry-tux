from abc import ABC, abstractmethod

from angrytux.model.game_objects.Missile import Missile

from angrytux.model.game_objects.Position import Position


class AbstractFactory(ABC):
    @abstractmethod
    def create_enemy(self):
        pass


    @abstractmethod
    def create_missile(self, position: Position, speed: float, movement_angle: float) -> Missile:
        pass
