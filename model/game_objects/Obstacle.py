from model.game_objects.obstacle_states.NewState import NewState
from .GameObject import GameObject
from .Position import Position

INITIAL_HIT_POINTS = 3


class Obstacle(GameObject):
    def __init__(self, position: Position):
        super().__init__(position)

        self.__hit_points = INITIAL_HIT_POINTS
        self.__state = NewState(self)


    def got_hit(self):
        self.__hit_points -= 1


    def collision_distance(self) -> float:
        return 50.


    def accept(self, visitor):
        visitor.visit(self)


    @property
    def hit_points(self):
        return self.__hit_points


    @property
    def state(self):
        return self.__state


    @state.setter
    def state(self, state):
        self.__state = state


    @property
    def points(self):
        return 0


    def __str__(self):
        return 'Obstacle'
