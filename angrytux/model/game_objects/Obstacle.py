from angrytux.model.game_objects.obstacle_states.NewState import NewState
from angrytux.model.game_objects.obstacle_states.ObstacleState import ObstacleState
from .GameObject import GameObject
from .Position import Position

INITIAL_HIT_POINTS = 3


class Obstacle(GameObject):
    """
    Class for game obstacle
    """


    def __init__(self, position: Position):
        """
        Create new obstacle
        :param position: initial position of obstacle
        """
        super().__init__(position)

        self.__hit_points = INITIAL_HIT_POINTS
        self.__state = NewState(self)


    def got_hit(self) -> None:
        """
        Obstacle got hit. Inform obstacle state
        """
        self.__state.hit()


    @property
    def collision_distance(self) -> float:
        """
        Collision distance of obstacle
        :return: 50. for this image
        """
        return 50.


    def accept(self, visitor) -> None:
        """
        Accept visitor for visitor pattern
        :param visitor: visitor object
        :return:
        """
        visitor.visit(self)


    @property
    def hit_points(self) -> int:
        """
        Get actual hit points of obstacle
        :return: current value of hit points
        """
        return self.__hit_points


    @hit_points.setter
    def hit_points(self, hit_points: int) -> None:
        """
        Set new value of hit points for obstacle
        :param hit_points: new value of hit points
        """
        self.__hit_points = hit_points


    @property
    def state(self) -> ObstacleState:
        """
        Get current state of obstacle
        :return: obstacle state
        """
        return self.__state


    @state.setter
    def state(self, state: ObstacleState) -> None:
        """
        Set new state for obstacle
        :param state: new state of obstacle
        """
        self.__state = state


    @property
    def points(self) -> int:
        """
        Points for hit obstacle
        :return: 0
        """
        return 0


    def __str__(self):
        return 'Obstacle'
