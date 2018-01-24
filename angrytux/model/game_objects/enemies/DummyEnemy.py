from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.enemy_states.DumpLiveState import DumpLiveState

from angrytux.model.game_objects.enemies.Enemy import Enemy


class DummyEnemy(Enemy):
    def __init__(self, position: Position):
        super().__init__(position)
        self._state = DumpLiveState(self)


    @property
    def collision_distance(self) -> float:
        """
        Collision distance for DummyEnemy because of size of image
        :return: 40 for this image
        """
        return 40


    @property
    def points(self) -> int:
        """
        Points for destroying this enemy
        :return: 10 point for this enemy
        """
        return 10
