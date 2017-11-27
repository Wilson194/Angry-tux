from angrytux.model.abstract_facotry.AbstractFactory import AbstractFactory
from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Position import Position

from angrytux.model.game_objects.missile_strategies.SimpleMove import SimpleMove


class SimpleFactory(AbstractFactory):
    def __init__(self):
        self.__missile_strategy = SimpleMove()


    def create_enemy(self):
        pass


    def create_missile(self, position: Position, speed: float, movement_angle: float) -> Missile:
        missile = Missile(position, speed, movement_angle, self.__missile_strategy)
        return missile
