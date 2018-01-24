from angrytux.model.game_objects.enemies.enemy_states.DeadState import DeadState

from angrytux.model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class HittedState(EnemyState):
    def __init__(self, enemy):
        super().__init__(enemy)
        #               FPS * seconds
        self.live_time = 60 * 0.5


    def move(self) -> bool:
        """
        By the timer, change state and move or don't move
        :return: True if change state, False otherwise
        """
        self.live_time -= 1

        if self.live_time == 0:
            self._enemy.state = DeadState(self._enemy)
            return True

        return False


    def hit(self) -> None:
        """
        Method for hit this enemy (what to do when hitted)
        Do nothing
        """
        pass


    @property
    def delete(self) -> bool:
        return False


    @property
    def collidable(self) -> bool:
        """
        Determinate if this object could collied with missile
        :return: True if collide, False otherwise
        """
        return False
