import os

import pygame
from angrytux.model.Levels.LevelCreator import LevelCreator
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.game_objects.Position import Position

from angrytux.model.game_objects.Obstacle import Obstacle


class Level1Creator(LevelCreator):
    """
    Level creator for level 1
    """


    def create_obstacles(self) -> list:
        """
        Create all obstacles for level 1
        :return: list of obstacles
        """
        obstacles = []

        obstacles.append(Obstacle(Position(400, 400)))
        obstacles.append(Obstacle(Position(690, 380)))
        obstacles.append(Obstacle(Position(490, 500)))
        obstacles.append(Obstacle(Position(300, 200)))

        return obstacles


    def create_enemies(self) -> list:
        """
        Create all enemies for level 1
        :return: list of enemies
        """
        enemies = []

        enemies.append(CreationFactory().create_dummy_enemy(Position(420, 400)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(700, 380)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(320, 750)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(560, 150)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(750, 220)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(750, 700)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(500, 500)))
        enemies.append(CreationFactory().create_dummy_enemy(Position(820, 300)))

        return enemies


    def music(self) -> None:
        """
        Linux music for level 1
        """
        file = os.path.join('angrytux', 'resources', 'sounds', 'song1.mp3')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
