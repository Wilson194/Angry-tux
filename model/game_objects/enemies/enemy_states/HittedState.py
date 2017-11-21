from model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class HittedState(EnemyState):
    def hit(self):
        pass


    @property
    def delete(self) -> bool:
        return False
