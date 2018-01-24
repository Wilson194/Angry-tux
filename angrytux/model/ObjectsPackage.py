import pickle

from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Obstacle import Obstacle

from angrytux.model.game_objects.enemies.Enemy import Enemy


class ObjectsPackage:
    """
    Class that handle all game object for packing to memento
    """


    def __init__(self):
        self.__missiles = []
        self.__enemies = []
        self.__obstacles = []


    def create_pack(self):
        """
        Create pickle memento of this object
        :return: pickle dump object
        """
        return pickle.dumps(vars(self))


    def set_pack(self, pack) -> None:
        """
        Unpack memento and set items to this object
        :param pack: pickle pack
        """
        previous_state = pickle.loads(pack)
        vars(self).clear()
        vars(self).update(previous_state)


    @property
    def missiles(self) -> list:
        """
        Getter for missiles
        :return: list of missiles
        """
        return self.__missiles


    @property
    def enemies(self) -> list:
        """
        Getter for enemies
        :return: list of enemies
        """
        return self.__enemies


    @property
    def obstacles(self) -> list:
        """
        Getter for obstacles
        :return: list of obstacles
        """
        return self.__obstacles


    @missiles.setter
    def missiles(self, missiles: list) -> None:
        """
        Setter for missiles
        :param missiles: list of missiles
        """
        self.__missiles = missiles


    @enemies.setter
    def enemies(self, enemies: list) -> None:
        """
        Setter for enemies
        :param enemies: list of enemies
        """
        self.__enemies = enemies


    @obstacles.setter
    def obstacles(self, obstacles: list) -> None:
        """
        Setter for obstacles
        :param obstacles: list of obstacles
        """
        self.__obstacles = obstacles


    def add_missile(self, missile: Missile) -> None:
        """
        Add one missile to list
        :param missile: missile object
        """
        self.__missiles.append(missile)


    def add_enemy(self, enemy: Enemy) -> None:
        """
        Add one enemy to list
        :param enemy: enemy object
        """
        self.__enemies.append(enemy)


    def add_obstacle(self, obstacle: Obstacle) -> None:
        """
        Add one obstacle to list
        :param obstacle: obstacle object
        """
        self.__obstacles.append(obstacle)


    def get_all_objects(self) -> list:
        """
        Get one list of all objects together
        :return: list of all objects
        """
        game_objects = []

        game_objects.extend(self.__missiles)
        game_objects.extend(self.__enemies)
        game_objects.extend(self.__obstacles)

        return game_objects


    def get_all_collidable_objects(self) -> list:
        """
        Get list of all collidable objects
        :return: list of all collidable objects
        """
        game_objects = []

        game_objects.extend([enemy for enemy in self.__enemies if enemy.state.collidable])
        game_objects.extend(self.__obstacles)

        return game_objects
