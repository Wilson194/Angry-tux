from model.abstract_facotry.AbstractFactory import AbstractFactory
from model.game_objects.Missile import Missile
from model.game_objects.Position import Position
from model.game_objects.missile_strategies.GravityMove import GravityMove


class RealisticFactory(AbstractFactory):
    def __init__(self):
        self.__missile_strategy = GravityMove()


    def create_enemy(self):
        pass


    def create_missile(self, position: Position, speed: float, movement_angle: float) -> Missile:
        missile = Missile(position, speed, movement_angle, self.__missile_strategy)
        return missile
