import os
import pygame

from model.Levels.LevelCreator import LevelCreator
from model.game_objects.Obstacle import Obstacle
from model.game_objects.Position import Position
from model.game_objects.enemies.DumpEnemy import DumpEnemy
from model.game_objects.enemies.MovingEnemy import MovingEnemy
from model.game_objects.enemies.SmartEnemy import SmartEnemy


class Level1Creator(LevelCreator):
    def create_obstacles(self) -> list:
        obstacles = []

        obstacles.append(Obstacle(Position(350, 400)))

        return obstacles


    def create_enemies(self) -> list:
        enemies = []

        # enemies.append(DumpEnemy(Position(400, 400)))
        # enemies.append(DumpEnemy(Position(200, 150)))
        # enemies.append(DumpEnemy(Position(600, 300)))
        # enemies.append(DumpEnemy(Position(400, 700)))
        enemies.append(DumpEnemy(Position(600, 500)))
        enemies.append(SmartEnemy(Position(600, 350)))
        enemies.append(MovingEnemy(Position(400, 400)))

        return enemies


    def music(self):
        file = os.path.join('resources', 'sounds', 'song1.mp3')
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
