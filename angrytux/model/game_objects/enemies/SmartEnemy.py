from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.enemy_states.SmartLiveState import SmartLiveState

from angrytux.model.game_objects.enemies.Enemy import Enemy


class SmartEnemy(Enemy):
    def __init__(self, position: Position):
        super().__init__(position)
        self._state = SmartLiveState(self)


    @property
    def collision_distance(self) -> float:
        """
        Collision distance for DummyEnemy because of size of image
        :return: 50 for this image
        """
        return 50.


    @property
    def points(self) -> int:
        """
        Points for destroying this enemy
        :return: 30 point for this enemy
        """
        return 30
