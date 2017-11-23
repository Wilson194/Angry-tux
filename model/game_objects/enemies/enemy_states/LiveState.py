import os
import pygame

from model.game_objects.enemies.enemy_states.EnemyState import EnemyState
from model.game_objects.enemies.enemy_states.HittedState import HittedState


class LiveState(EnemyState):
    def __init__(self, enemy):
        super().__init__(enemy)


    def move(self) -> bool:
        return False


    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join('resources', 'sounds', 'blue_screen.wav')))

        self._enemy.state = HittedState(self._enemy)
