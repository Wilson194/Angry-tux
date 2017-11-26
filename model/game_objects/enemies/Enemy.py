from model.game_objects.GameObject import GameObject
from abc import ABC, abstractmethod

from model.game_objects.Position import Position
from model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class Enemy(GameObject, ABC):
    def __init__(self, position: Position):
        super().__init__(position)


    @abstractmethod
    def collision_distance(self):
        pass


    @property
    def state(self):
        return self._state


    @state.setter
    def state(self, state: EnemyState):
        self._state = state


    def accept(self, visitor):
        visitor.visit(self)


    def __str__(self):
        return 'Enemy'
