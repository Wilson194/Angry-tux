import pickle

from model.game_objects.Missile import Missile
from model.game_objects.Obstacle import Obstacle
from model.game_objects.enemies.Enemy import Enemy


class ObjectsPackage:
    def __init__(self):
        self.__missiles = []
        self.__enemies = []
        self.__obstacles = []


    def create_pack(self):
        return pickle.dumps(vars(self))


    def set_pack(self, pack):
        previous_state = pickle.loads(pack)
        vars(self).clear()
        vars(self).update(previous_state)


    @property
    def missiles(self):
        return self.__missiles


    @property
    def enemies(self):
        return self.__enemies


    @property
    def obstacles(self):
        return self.__obstacles


    @missiles.setter
    def missiles(self, missiles: list):
        self.__missiles = missiles


    @enemies.setter
    def enemies(self, enemies: list):
        self.__enemies = enemies


    @obstacles.setter
    def obstacles(self, obstacles: list):
        self.__obstacles = obstacles


    def add_missile(self, missile: Missile):
        self.__missiles.append(missile)


    def add_enemy(self, enemy: Enemy):
        self.__enemies.append(enemy)


    def add_obstacle(self, obstacle: Obstacle):
        self.__obstacles.append(obstacle)


    def get_all_objects(self):
        game_objects = []

        game_objects.extend(self.__missiles)
        game_objects.extend(self.__enemies)
        game_objects.extend(self.__obstacles)

        return game_objects


    def get_all_collidable_objects(self):
        game_objects = []

        game_objects.extend(self.__enemies)
        game_objects.extend(self.__obstacles)

        return game_objects
