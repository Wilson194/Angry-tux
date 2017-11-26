from model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class DeadState(EnemyState):
    @property
    def collidable(self) -> bool:
        return False


    def hit(self):
        pass


    def move(self) -> bool:
        return False


    @property
    def delete(self) -> bool:
        return True
