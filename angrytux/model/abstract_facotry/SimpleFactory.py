from angrytux.model.abstract_facotry.AbstractFactory import AbstractFactory
from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.DummyEnemy import DummyEnemy

from angrytux.model.game_objects.missile_strategies.SimpleMove import SimpleMove


class SimpleFactory(AbstractFactory):
    """
    Simple factory for creating enemies and missiles
    Missiles:
            - simple lowering angle

    Smart enemy:
            - dump enemy sitting at one place
    Dummy enemy:
            - dump enemy sitting at one place
    """
    def __init__(self):
        self.__missile_strategy = SimpleMove()


    def create_missile(self, position: Position, speed: float, movement_angle: float) -> Missile:
        missile = Missile(position, speed, movement_angle, self.__missile_strategy)
        return missile


    def create_smart_enemy(self, position: Position):
        enemy = DummyEnemy(position)
        return enemy


    def create_dummy_enemy(self, position: Position):
        enemy = DummyEnemy(position)
        return enemy
