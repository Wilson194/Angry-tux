import os
import pygame

from config.Config import Config
from model.game_objects.enemies.enemy_states.EnemyState import EnemyState
from model.game_objects.enemies.enemy_states.HittedState import HittedState


class MovingLiveState(EnemyState):
    def __init__(self, enemy):
        super().__init__(enemy)
        self.__operator = 90


    def move(self) -> bool:
        x, y = self._enemy.position.to_rect()

        # y += self.__operator

        if y > Config()['windows_size'][1] - 20 or y < 70:
            self.__operator = -self.__operator

        self._enemy.position.move(self.__operator, 3)

        return True


    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join('resources', 'sounds', 'blue_screen.wav')))

        self._enemy.state = HittedState(self._enemy)


    @property
    def collidable(self) -> bool:
        return True
