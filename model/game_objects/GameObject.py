from abc import ABC, abstractmethod

from model.Visitor.IVisitable import IVisitable
from .Position import Position


class GameObject(IVisitable, ABC):
    def __init__(self, position: Position):
        self.__position = position


    @property
    def position(self):
        return self.__position


    @abstractmethod
    def collision_distance(self):
        pass


    def has_collided_with(self, game_object) -> bool:
        sum_collision_distance = self.collision_distance() + game_object.collision_distance()

        distance = self.__position.compute_distance_from(game_object.position)

        return distance < sum_collision_distance
