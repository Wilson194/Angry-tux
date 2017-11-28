from angrytux.model.game_objects.obstacle_states.HittedState import HittedState

from angrytux.model.game_objects.obstacle_states.ObstacleState import ObstacleState


class NewState(ObstacleState):
    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        self._obstacle.hit_points -= 1
        self._obstacle.state = HittedState(self._obstacle)
