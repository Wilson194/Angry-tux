from abc import ABC, abstractmethod

from angrytux.model.game_objects.Missile import Missile

from angrytux.model.game_objects.Position import Position


class AbstractFactory(ABC):
    """
    Abstract class for factories
    """


    @abstractmethod
    def create_smart_enemy(self, position: Position):
        """
        Create some smart enemy
        :param position: position of enemy
        :return:
        """
        pass


    @abstractmethod
    def create_dummy_enemy(self, position: Position):
        """
        Create some dummy enemy
        :param position: position of enemy
        :return:
        """


    @abstractmethod
    def create_missile(self, position: Position, speed: float, movement_angle: float) -> Missile:
        pass
