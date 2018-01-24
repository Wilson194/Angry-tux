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
        """
        Create one missile.
        :param position: starting position of missile
        :param speed: starting speed of missile
        :param movement_angle: starting moving angle of missile
        :return: New missile ready for moving
        """
        missile = Missile(position, speed, movement_angle, self.__missile_strategy)
        return missile


    def create_smart_enemy(self, position: Position):
        """
        Create one smart enemy. This enemy just sitting at one place
        :param position: starting position
        :return: New created smart enemy
        """
        enemy = DummyEnemy(position)
        return enemy


    def create_dummy_enemy(self, position: Position):
        """
        Create one dummy enemy. This enemy just sitting at one place
        :param position: starting position
        :return: New created dummy enemy
        """
        enemy = DummyEnemy(position)
        return enemy
