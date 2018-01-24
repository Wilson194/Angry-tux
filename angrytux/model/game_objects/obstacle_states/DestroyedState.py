from angrytux.model.game_objects.obstacle_states.ObstacleState import ObstacleState


class DestroyedState(ObstacleState):
    @property
    def delete(self) -> bool:
        """
        Remove by garbage collector
        :return: True
        """
        return True


    def hit(self) -> None:
        """
        Do nothing
        """
        pass
