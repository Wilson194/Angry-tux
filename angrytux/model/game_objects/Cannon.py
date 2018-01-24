from angrytux.config.Config import Config
from angrytux.model.game_objects.cannon_states.CannonState import CannonState
from .GameObject import GameObject
from .Position import Position
from .cannon_states.SingleShoot import SingleShoot


class Cannon(GameObject):
    """
    Cannon object. This is object for cannon in game.
    """


    def __init__(self, position: Position):
        super().__init__(position)
        self.__shooting_angle = Config()['cannon_initial_shooting_angle']
        self.__strength = Config()['cannon_initial_strength']
        self.__state = SingleShoot(self)


    @property
    def shooting_angle(self) -> float:
        """
        Get starting angle of missile
        :return: shooting angle
        """
        return self.__shooting_angle


    @shooting_angle.setter
    def shooting_angle(self, value: float) -> None:
        """
        Setter for shooting angle
        :param value: new shooting angle
        """
        self.__shooting_angle = value


    @property
    def strength(self) -> float:
        """
        Get initial strength for missiles
        :return: value of initial strength
        """
        return self.__strength


    @strength.setter
    def strength(self, value: float):
        """
        Cannon strength setter, min and max defined by config
        cannon_min_strength, cannon_max_strength
        :param value: value of new strength
        """
        if value < Config()['cannon_min_strength']:
            self.__strength = Config()['cannon_min_strength']
        elif value > Config()['cannon_max_strength']:
            self.__strength = Config()['cannon_max_strength']
        else:
            self.__strength = value


    def shoot(self) -> tuple:
        """
        Create new missiles in game
        :return: tuple of created missiles
        """
        return self.__state.shoot()


    @property
    def collision_distance(self):
        """
        Collision distance of cannon
        :return: zero because cannon don't collide
        """
        return 0


    @property
    def state(self) -> CannonState:
        """
        Getter of actual state of cannon
        :return: actual cannon state
        """
        return self.__state


    @state.setter
    def state(self, state: CannonState) -> None:
        """
        Set new cannon state
        :param state: new cannon state
        """
        self.__state = state


    def accept(self, visitor) -> None:
        """
        Accept visitor for drawing this object
        :param visitor: visitor object
        """
        visitor.visit(self)


    def angle(self, angle: float) -> None:
        """
        Change angle of the cannon. Change the angle by value of angle
        :param angle: value of changed angle
        """
        if Config()['max_shooting_angle'] > angle + self.shooting_angle > Config()['min_shooting_angle']:
            self.shooting_angle += angle


    def change_state(self) -> None:
        """
        Change state of cannon. State change based on current state
        """
        self.state.change_state()


    def move(self, angle, distance) -> None:
        """
        Move the cannon by distance in direction of angle
        + -> up
        - -> down
        :param angle: +/- 90 up or down
        :param distance: distance of move
        """
        if 10 < self.position.y_position + (distance * -angle / 90) < Config()['windows_size'][1] - 100:
            self.position.move(angle, distance)


    def __str__(self):
        return 'Cannon'
