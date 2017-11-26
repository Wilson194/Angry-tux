from abc import ABC, abstractmethod


class LevelCreator(ABC):
    @abstractmethod
    def create_enemies(self) -> list:
        pass


    @abstractmethod
    def create_obstacles(self) -> list:
        pass


    @property
    @abstractmethod
    def music(self):
        pass
