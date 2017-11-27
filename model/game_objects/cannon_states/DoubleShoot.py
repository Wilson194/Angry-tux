import os
import pygame

from model.abstract_facotry.CreationFactory import CreationFactory
from model.game_objects.Position import Position
from model.game_objects.cannon_states.CannonState import CannonState


class DoubleShoot(CannonState):
    def __init__(self, cannon):
        self.__cannon = cannon


    def shoot(self):
        x = self.__cannon.position.x_position + 105
        y = self.__cannon.position.y_position + 55 - self.__cannon.shooting_angle

        pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join('resources', 'sounds', 'shoot.wav')))
        missile1 = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle - 20)
        missile2 = CreationFactory().create_missile(Position(x, y), self.__cannon.strength, self.__cannon.shooting_angle + 20)

        return missile1, missile2


    def __eq__(self, other):
        if type(other) is str and other.lower() == 'doubleshoot':
            return True

        return False
