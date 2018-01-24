from abc import ABC, abstractmethod

from angrytux.model.game_objects.GameObject import GameObject
from angrytux.model.game_objects.Position import Position

from angrytux.model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class Enemy(GameObject, ABC):
    """
    Interface for enemy
    """


    def __init__(self, position: Position):
        super().__init__(position)


    @property
    @abstractmethod
    def collision_distance(self) -> float:
        """
        Value of this object, collide with another object
        :return:
        """
        pass


    @property
    def state(self) -> EnemyState:
        """
        Get state of enemy
        :return: current state of enemy
        """
        return self._state


    @state.setter
    def state(self, state: EnemyState) -> None:
        """
        Set new state for enemy
        :param state: new enemy state
        """
        self._state = state


    def accept(self, visitor) -> None:
        """
        Method for visitor pattern. Accept the visitor
        :param visitor: actual visitor object
        """
        visitor.visit(self)


    def __str__(self):
        return 'Enemy'
