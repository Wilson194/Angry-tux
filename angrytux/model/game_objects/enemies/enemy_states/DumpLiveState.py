import os
import pygame
from angrytux.model.game_objects.enemies.enemy_states.HittedState import HittedState
from angrytux.model.game_objects.enemies.enemy_states.EnemyState import EnemyState
import angrytux.main


class DumpLiveState(EnemyState):
    def __init__(self, enemy):
        super().__init__(enemy)


    def move(self) -> bool:
        return False


    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join(angrytux.main.RESOURCES_DIR, 'sounds', 'blue_screen.wav')))

        self._enemy.state = HittedState(self._enemy)


    @property
    def collidable(self) -> bool:
        return True
