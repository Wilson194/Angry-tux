from abc import ABC, abstractmethod


class EnemyState(ABC):
    def __init__(self, enemy):
        self._enemy = enemy


    @property
    @abstractmethod
    def delete(self) -> bool:
        pass


    @abstractmethod
    def hit(self):
        pass


    @abstractmethod
    def move(self) -> bool:
        pass


    @property
    @abstractmethod
    def collidable(self) -> bool:
        pass