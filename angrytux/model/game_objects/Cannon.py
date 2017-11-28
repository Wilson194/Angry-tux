from angrytux.config.Config import Config
from angrytux.model.game_objects.cannon_states.CannonState import CannonState
from .GameObject import GameObject
from .Position import Position
from .cannon_states.DoubleShoot import DoubleShoot
from .cannon_states.SingleShoot import SingleShoot

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
        if value < Config()['min_strength']:
            self.__strength = Config()['min_strength']
        elif value > Config()['max_strength']:
            self.__strength = Config()['max_strength']
        else:
            self.__strength = value


    def shoot(self) -> tuple:
        return self.__state.shoot()


    @property
    def collision_distance(self):
        return 0


    @property
    def state(self):
        return self.__state


    @state.setter
    def state(self, state: CannonState):
        self.__state = state


    def accept(self, visitor):
        visitor.visit(self)


    def angle(self, angle):
        if Config()['max_shooting_angle'] > angle + self.shooting_angle > Config()['min_shooting_angle']:
            self.shooting_angle += angle


    def change_state(self):
        self.state.change_state()


    def move(self, angle, distance):
        if 10 < self.position.y_position + (distance * -angle / 90) < Config()['windows_size'][1] - 100:
            self.position.move(angle, distance)


    def __str__(self):
        return 'Cannon'
