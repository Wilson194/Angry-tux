from model.game_objects.enemies.enemy_states.EnemyState import EnemyState
from model.game_objects.enemies.enemy_states.HittedState import HittedState


class LiveState(EnemyState):
    @property
    def delete(self) -> bool:
        return False


    def hit(self):
        self._enemy.state = HittedState(self._enemy)
