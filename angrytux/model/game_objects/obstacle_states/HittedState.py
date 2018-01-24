from angrytux.model.game_objects.obstacle_states.DestroyedState import DestroyedState

from angrytux.model.game_objects.obstacle_states.ObstacleState import ObstacleState


class HittedState(ObstacleState):
    @property
    def delete(self) -> bool:
        """
        Don't delete this obstacle
        :return: False
        """
        return False


    def hit(self) -> None:
        """
        Based on hit points, decrease hit points or change state
        """
        self._obstacle.hit_points -= 1

        if self._obstacle.hit_points == 0:
            self._obstacle.state = DestroyedState(self._obstacle)
