
from .GameObject import GameObject
from abc import ABC, abstractmethod


class Enemy(GameObject, ABC):
    @abstractmethod
    def collision_distance(self):
        pass


    def accept(self, visitor):
        visitor.visit(self)


    def __str__(self):
        return 'Enemy'


class DumpEnemy(Enemy):
    def collision_distance(self) -> float:
        return 50.
1

class SmartEnemy(Enemy):
    def collision_distance(self) -> float:
        return 50.
