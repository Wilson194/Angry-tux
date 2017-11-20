from model.game_objects.cannon_states.CannonState import CannonState
from model.game_objects.Missile import Missile
from model.game_objects.Position import Position


class SingleShoot(CannonState):
    def __init__(self, cannon):
        self.__cannon = cannon


    def shoot(self) -> tuple:
        x = self.__cannon.position.x_position + 100
        y = self.__cannon.position.y_position - 40
        missile = Missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle)

        return missile,
