from abc import ABC, abstractmethod

from angrytux.model.Visitor.IVisitable import IVisitable
from .Position import Position


class GameObject(IVisitable, ABC):
    """
    Based object for all game objects. Define based attributes and functions
    All game objects are visitable because of drawing
    """


    def __init__(self, position: Position):
        self.__position = position


    @property
    def position(self) -> Position:
        """
        Get actual position of object
        :return: Position object with actual position
        """
        return self.__position


    @position.setter
    def position(self, position: Position) -> None:
        """
        Set new position of object
        :param position: new Position object
        """
        self.__position = position


    @property
    @abstractmethod
    def collision_distance(self) -> float:
        """
        Collision distance of object. Define distance between two object whe they collide
        :return: collision distance
        """
        pass


    def has_collided_with(self, game_object) -> bool:
        """
        Function that determinate, if game object collided with another object
        :param game_object: another object for collision
        :return: True if collided False otherwise
        """
        sum_collision_distance = self.collision_distance + game_object.collision_distance

        distance = self.__position.compute_distance_from(game_object.position)

        return distance < sum_collision_distance
