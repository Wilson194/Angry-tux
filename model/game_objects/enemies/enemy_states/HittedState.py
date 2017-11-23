from model.game_objects.enemies.enemy_states.DeadState import DeadState
from model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class HittedState(EnemyState):
    def __init__(self, enemy):
        super().__init__(enemy)
        #               FPS * seconds
        self.live_time = 60 * 0.5


    def move(self) -> bool:
        self.live_time -= 1

        if self.live_time == 0:
            self._enemy.state = DeadState(self._enemy)
            return True

        return False


    def hit(self):
        pass


    @property
    def delete(self) -> bool:
        return False
