from model.abstract_facotry.CreationFactory import CreationFactory
from model.game_objects.Position import Position
from model.game_objects.cannon_states.CannonState import CannonState


class DoubleShoot(CannonState):
    def __init__(self, cannon):
        self.__cannon = cannon


    def shoot(self):
        x = self.__cannon.position.x_position + 100
        y = self.__cannon.position.y_position + 27

        missile1 = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle - 20)
        missile2 = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle + 20)

        return missile1, missile2
