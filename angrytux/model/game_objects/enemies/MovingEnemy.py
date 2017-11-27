from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.enemy_states.MovingLiveState import MovingLiveState

from angrytux.model.game_objects.enemies.Enemy import Enemy


class MovingEnemy(Enemy):
    def __init__(self, position: Position):
        super().__init__(position)
        self._state = MovingLiveState(self)


    @property
    def collision_distance(self) -> float:
        return 50.


    @property
    def points(self):
        return 30
