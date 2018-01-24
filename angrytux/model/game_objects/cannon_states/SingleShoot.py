import os

import pygame
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.game_objects.cannon_states.CannonState import CannonState

from angrytux.model.game_objects.Position import Position


class SingleShoot(CannonState):
    def __init__(self, cannon):
        self.__cannon = cannon


    def shoot(self) -> tuple:
        """
        Shoot one missile
        :return: tuple with only one missile
        """
        x = self.__cannon.position.x_position + 105
        y = self.__cannon.position.y_position + 55 - self.__cannon.shooting_angle
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('angrytux', 'resources', 'sounds', 'shoot.wav')))
        missile = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle)

        return missile,


    def change_state(self) -> None:
        """
        Change state from SingleShoot to DoubleShoot
        """
        from angrytux.model.game_objects.cannon_states.DoubleShoot import DoubleShoot
        self.__cannon.state = DoubleShoot(self.__cannon)


    @property
    def points_multiple(self):
        """
        Number of score multiple when this mode is enable
        :return: for double shoot is 1
        """
        return 1


    @property
    def shoot_cost(self):
        """
        Number of points that cost one shoot
        :return: for double shoot is 2
        """
        return 2


    def __eq__(self, other):
        if type(other) is str and other.lower() == 'singleshoot':
            return True

        return False
