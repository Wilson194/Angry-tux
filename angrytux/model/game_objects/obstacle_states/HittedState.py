from angrytux.model.game_objects.obstacle_states.DestroyedState import DestroyedState

from angrytux.model.game_objects.obstacle_states.ObstacleState import ObstacleState


class HittedState(ObstacleState):
    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        self._obstacle.got_hit()

        if self._obstacle.hit_points == 0:
            self._obstacle.state = DestroyedState(self._obstacle)
