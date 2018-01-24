from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.Enemy import Enemy
from angrytux.model.game_objects.enemies.MovingEnemy import MovingEnemy
from angrytux.model.game_objects.enemies.SmartEnemy import SmartEnemy
from angrytux.model.game_objects.missile_strategies.GravityMove import GravityMove

from angrytux.model.abstract_facotry.AbstractFactory import AbstractFactory


class RealisticFactory(AbstractFactory):
    """
    Realistic factory for creating enemies and missiles
    Missiles:
            - moving based on gravity
            - moving more like ballistic ellipse

    Smart enemy:
            - teleporting enemy based on time
    Dummy enemy:
            - moving enemy on line
    """


    def __init__(self):
        self.__missile_strategy = GravityMove()


    def create_missile(self, position: Position, speed: float, movement_angle: float) -> Missile:
        """
        Create one realistic missile. Missile moving based on gravity and ballistic ellipse
        :param position: starting position
        :param speed: starting speed (based on cannon strength)
        :param movement_angle: starting moving angle
        :return: Missile object ready for moving
        """
        missile = Missile(position, speed, movement_angle, self.__missile_strategy)
        return missile


    def create_smart_enemy(self, position: Position) -> SmartEnemy:
        """
        Create one smart enemy. Smart enemy can teleport after short time.
        :param position: Starting position of enemy
        :return: Created smart enemy
        """
        enemy = SmartEnemy(position)
        return enemy


    def create_dummy_enemy(self, position: Position) -> MovingEnemy:
        """
        Create one dummy enemy. This enemy can move only at one straight line
        :param position: Starting position of enemy
        :return: Created moving enemy
        """
        enemy = MovingEnemy(position)
        return enemy
