from model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class DeadState(EnemyState):
    @property
    def delete(self) -> bool:
        return True
