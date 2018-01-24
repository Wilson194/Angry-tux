from angrytux.model.game_objects.missile_states.Collided import Collided
from angrytux.model.game_objects.missile_states.MissileState import MissileState
from angrytux.model.game_objects.missile_states.OutOfGame import OutOfGame

from angrytux.model.game_objects.missile_states.Flying import Flying
from .GameObject import GameObject
from .Position import Position
from .missile_strategies.MissileStrategy import MissileStrategy


class Missile(GameObject):
    """
    Class for handling one missile object.
    """


    def __init__(self, position: Position, speed: float, movement_angle: float, strategy: MissileStrategy = None):
        """
        Create new missile
        :param position: starting position of missile
        :param speed: starting speed of missile
        :param movement_angle: Starting movement angle of missile
        :param strategy: moving strategy of missile
        """
        super().__init__(position)

        self.__speed = speed
        self.__movement_angle = movement_angle
        self.__strategy = strategy
        self.__position = position
        self.__state = Flying()


    @property
    def collision_distance(self):
        """
        Missile have collision distance 1, because all obstacles and enemies have collision distance
        :return: 1
        """
        return 1


    def move(self, gravity: float, collidable_objects: list) -> int:
        """
        Move missile by one tick of clock
        :param gravity: current value of gravity
        :param collidable_objects: list of all collidable object in game
        :return: Number of points, if something is hitted
        """
        points = 0

        self.__strategy.move(self, gravity)

        out = self.__position.out_of_window()

        if out:
            self.__state = OutOfGame()

        for obj in collidable_objects:
            if self.has_collided_with(obj):
                self.__state = Collided()
                obj.state.hit()
                points += obj.points

        return points


    def accept(self, visitor) -> None:
        """
        Accept function for visitor pattern
        :param visitor: visitor object
        """
        visitor.visit(self)


    @property
    def state(self) -> MissileState:
        """
        Get current state of missile
        :return: current missile state
        """
        return self.__state


    @property
    def movement_angle(self) -> float:
        """
        Get current movement angle of missile
        :return: angle of missile
        """
        return self.__movement_angle


    @movement_angle.setter
    def movement_angle(self, angle: float) -> None:
        """
        Set new movement angle of missile
        :param angle: new angle of missile
        """
        self.__movement_angle = angle


    @property
    def speed(self) -> float:
        """
        Get current speed of missile
        :return: current speed of missile
        """
        return self.__speed


    @speed.setter
    def speed(self, speed: float) -> None:
        """
        Set new speed for missile
        :param speed: new speed of missile
        """
        self.__speed = speed


    def __str__(self):
        return 'Missile'
