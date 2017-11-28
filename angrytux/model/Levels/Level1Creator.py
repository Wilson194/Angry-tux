import os

import pygame
from angrytux.model.Levels.LevelCreator import LevelCreator
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.DummyEnemy import DummyEnemy
from angrytux.model.game_objects.enemies.MovingEnemy import MovingEnemy
from angrytux.model.game_objects.enemies.SmartEnemy import SmartEnemy

from angrytux.model.game_objects.Obstacle import Obstacle


class Level1Creator(LevelCreator):
    def create_obstacles(self) -> list:
        obstacles = []

        obstacles.append(Obstacle(Position(350, 400)))

        return obstacles


    def create_enemies(self) -> list:
        enemies = []

        enemies.append(CreationFactory().create_smart_enemy(Position(600, 350)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(400, 400)))

        return enemies


    def music(self):
        file = os.path.join('angrytux', 'resources', 'sounds', 'song1.mp3')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
