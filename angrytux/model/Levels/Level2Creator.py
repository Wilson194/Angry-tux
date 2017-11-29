import os

import pygame
from angrytux.model.Levels.LevelCreator import LevelCreator
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.game_objects.Position import Position

from angrytux.model.game_objects.Obstacle import Obstacle


class Level2Creator(LevelCreator):
    def create_obstacles(self) -> list:
        obstacles = []

        for i in range(100, 800, 50):
            obstacles.append(Obstacle(Position(400, i)))
            obstacles.append(Obstacle(Position(520, i)))

        return obstacles


    def create_enemies(self) -> list:
        enemies = []

        enemies.append(CreationFactory().create_dummy_enemy(Position(450, 400)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(450, 200)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(450, 600)))

        enemies.append(CreationFactory().create_dummy_enemy(Position(570, 450)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(570, 250)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(570, 650)))

        enemies.append(CreationFactory().create_smart_enemy(Position(700, 700)))
        enemies.append(CreationFactory().create_smart_enemy(Position(800, 450)))
        enemies.append(CreationFactory().create_smart_enemy(Position(750, 100)))

        return enemies


    def music(self):
        file = os.path.join('angrytux', 'resources', 'sounds', 'song1.mp3')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
