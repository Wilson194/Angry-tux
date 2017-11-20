from .GameObject import GameObject
from .Position import Position
from .missile_strategies.MissileStrategy import MissileStrategy


class Missile(GameObject):
    def __init__(self, position: Position, speed: float, movement_angle: float, strategy: MissileStrategy = None):
        super().__init__(position)

        self.__speed = speed
        self.__movement_angle = movement_angle
        self.__strategy = strategy
        self.__position = position


    def collision_distance(self):
        return 50


    def move(self, gravity: float):
        self.__strategy.move(gravity, self.__position, self.__movement_angle, self.__speed)


    def accept(self, visitor):
        visitor.visit(self)


    @property
    def movement_angle(self):
        return self.__movement_angle


    def __str__(self):
        return 'Missile'
