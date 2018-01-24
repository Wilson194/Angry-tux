from abc import ABC, abstractmethod


class LevelCreator(ABC):
    """
    Class for generating level for game
    """


    @abstractmethod
    def create_enemies(self) -> list:
        """
        This method should create all enemies in level
        :return: list of enemies in level
        """
        pass


    @abstractmethod
    def create_obstacles(self) -> list:
        """
        This method should create all obstacles in level
        :return: list of obstacle in level
        """
        pass


    @property
    @abstractmethod
    def music(self) -> None:
        """
        This method should play music, which will play whole level
        """
        pass
