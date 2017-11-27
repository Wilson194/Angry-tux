from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.enemy_states.SmartLiveState import SmartLiveState

from angrytux.model.game_objects.enemies.Enemy import Enemy


class SmartEnemy(Enemy):
    def __init__(self, position: Position):
        super().__init__(position)
        self._state = SmartLiveState(self)


    def collision_distance(self) -> float:
        return 50.


    @property
    def points(self):
        return 30
