from angrytux.model.game_objects.obstacle_states.HittedState import HittedState

from angrytux.model.game_objects.obstacle_states.ObstacleState import ObstacleState


class NewState(ObstacleState):
    @property
    def delete(self) -> bool:
        """
        Don't delete this obstacle
        :return: False
        """
        return False


    def hit(self) -> None:
        """
        Just remove hit points of obstacle and change state
        """
        self._obstacle.hit_points -= 1
        self._obstacle.state = HittedState(self._obstacle)
