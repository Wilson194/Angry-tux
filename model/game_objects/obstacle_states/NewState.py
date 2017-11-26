from model.game_objects.obstacle_states.HittedState import HittedState
from model.game_objects.obstacle_states.ObstacleState import ObstacleState


class NewState(ObstacleState):
    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        self._obstacle.got_hit()
        self._obstacle.state = HittedState(self._obstacle)
