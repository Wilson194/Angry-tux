
from .GameObject import GameObject
from .Position import Position

INITIAL_HIT_POINTS = 3


class Obstacle(GameObject):
    def __init__(self, position: Position):
        super().__init__(position)

        self.__hit_points = INITIAL_HIT_POINTS


    def got_hit(self):
        self.__hit_points -= 1


    def collision_distance(self) -> float:
        return 50.


    def accept(self, visitor):
        visitor.visit(self)


    def __str__(self):
        return 'Obstacle'
