from model.game_objects.missile_states.Flying import Flying
from model.game_objects.missile_states.OutOfGame import OutOfGame
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
        self.__state = Flying()


    def collision_distance(self):
        return 50


    def move(self, gravity: float):
        self.__strategy.move(self, gravity)

        out = self.__position.out_of_window()

        if out:
            self.__state = OutOfGame()


    def accept(self, visitor):
        visitor.visit(self)


    @property
    def state(self):
        return self.__state


    @property
    def movement_angle(self):
        return self.__movement_angle


    @movement_angle.setter
    def movement_angle(self, angle):
        self.__movement_angle = angle


    @property
    def speed(self):
        return self.__speed


    def __str__(self):
        return 'Missile'
