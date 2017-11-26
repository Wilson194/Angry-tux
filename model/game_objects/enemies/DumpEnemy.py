from model.game_objects.Position import Position
from model.game_objects.enemies.Enemy import Enemy
from model.game_objects.enemies.enemy_states.DumpLiveState import DumpLiveState


class DumpEnemy(Enemy):
    def __init__(self, position: Position):
        super().__init__(position)
        self._state = DumpLiveState(self)


    def collision_distance(self) -> float:
        return 40


    @property
    def points(self):
        return 10
