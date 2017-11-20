from .GameObject import GameObject
from .Position import Position
from .cannon_states.SingleShoot import SingleShoot
from .cannon_states.DoubleShoot import DoubleShoot

INITIAL_STRENGTH = 5
INITIAL_SHOOTING_ANGLE = 0


class Cannon(GameObject):
    def __init__(self, position: Position):
        super().__init__(position)
        self.__shooting_angle = INITIAL_SHOOTING_ANGLE
        self.__strength = INITIAL_STRENGTH
        self.__state = SingleShoot(self)


    @property
    def shooting_angle(self):
        return self.__shooting_angle


    @shooting_angle.setter
    def shooting_angle(self, value):
        self.__shooting_angle = value


    @property
    def strength(self):
        return self.__strength


    @strength.setter
    def strength(self, value):
        if 10 > value > 1:
            self.__strength = value


    def shoot(self) -> tuple:
        return self.__state.shoot()


    @property
    def collision_distance(self):
        return 0


    def accept(self, visitor):
        visitor.visit(self)


    def angle(self, angle):
        if 80 > angle + self.shooting_angle > -110:
            self.shooting_angle += angle


    def change_state(self):
        if isinstance(self.__state, SingleShoot):
            self.__state = DoubleShoot(self)

        elif isinstance(self.__state, DoubleShoot):
            self.__state = SingleShoot(self)


    def __str__(self):
        return 'Cannon'
