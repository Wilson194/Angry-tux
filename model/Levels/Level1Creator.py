from model.Levels.LevelCreator import LevelCreator
from model.game_objects.Obstacle import Obstacle
from model.game_objects.Position import Position
from model.game_objects.enemies.DumpEnemy import DumpEnemy


class Level1Creator(LevelCreator):
    def create_obstacles(self) -> list:
        obstacles = []

        obstacles.append(Obstacle(Position(350, 400)))

        return obstacles


    def create_enemies(self) -> list:
        enemies = []

        enemies.append(DumpEnemy(Position(400, 400)))
        enemies.append(DumpEnemy(Position(200, 150)))
        enemies.append(DumpEnemy(Position(600, 300)))
        enemies.append(DumpEnemy(Position(400, 700)))

        return enemies
