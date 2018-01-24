import os

import pygame
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.game_objects.cannon_states.CannonState import CannonState

from angrytux.model.game_objects.Position import Position


class DoubleShoot(CannonState):
    def __init__(self, cannon):
        self.__cannon = cannon


    def shoot(self) -> tuple:
        """
        Shoot two missiles from cannon. Each another angle
        :return: tuple of two missiles
        """
        x = self.__cannon.position.x_position + 105
        y = self.__cannon.position.y_position + 55 - self.__cannon.shooting_angle

        pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('angrytux', 'resources', 'sounds', 'shoot.wav')))
        missile1 = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle - 20)
        missile2 = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle + 20)

        return missile1, missile2


    def change_state(self) -> None:
        """
        Change state from double shoot to single shoot
        """
        from angrytux.model.game_objects.cannon_states.SingleShoot import SingleShoot
        self.__cannon.state = SingleShoot(self.__cannon)


    @property
    def points_multiple(self) -> int:
        """
        Number of score multiple when this mode is enable
        :return: for double shoot is 2
        """
        return 2


    @property
    def shoot_cost(self) -> int:
        """
        Number of points that cost one shoot
        :return: for double shoot is 3
        """
        return 3


    def __eq__(self, other):
        if type(other) is str and other.lower() == 'doubleshoot':
            return True

        return False
