from .GameObject import GameObject
from .Position import Position


class Missile(GameObject):
    def __init__(self, position: Position, speed: float, movement_angle: float, strategy: object = None):
        super().__init__(position)

        self.__speed = speed
        self.__movement_angle = movement_angle
        self.__strategy = strategy


    def collision_distance(self):
        return 50


    def move(self, gravity: float):
        pass  # TODO, delegate to strategy


    def accept(self, visitor):
        visitor.visit(self)


    def __str__(self):
        return 'Missile'
