import os
import pygame
import random
import math

from config.Config import Config
from model.game_objects.Position import Position
from model.game_objects.enemies.enemy_states.EnemyState import EnemyState
from model.game_objects.enemies.enemy_states.HittedState import HittedState


class SmartLiveState(EnemyState):
    MOVE_TIME = 60 * 5


    def __init__(self, enemy):
        super().__init__(enemy)
        self.__time = self.MOVE_TIME
        self.__moving = False
        self.__target_position = None


    def move(self) -> bool:
        self.__time -= 1

        if self.__time == 0:
            position = self.__get_random_position()
            self._enemy.position = position
            self.__time = self.MOVE_TIME
            return True

        return False


    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join('resources', 'sounds', 'blue_screen.wav')))

        self._enemy.state = HittedState(self._enemy)


    @property
    def collidable(self) -> bool:
        return True


    def __get_random_position(self):
        x_from = 150
        x_to = Config()['windows_size'][0] - 50
        y_from = 150
        y_to = Config()['windows_size'][1] - 50
        position = Position(random.randint(x_from, x_to), random.randint(y_from, y_to))

        return position
