from model.game_objects.obstacle_states.ObstacleState import ObstacleState


class DestroyedState(ObstacleState):
    @property
    def delete(self) -> bool:
        return True


    def hit(self):
        pass
