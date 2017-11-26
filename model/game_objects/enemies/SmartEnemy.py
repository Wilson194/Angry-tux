from model.game_objects.enemies.Enemy import Enemy


class SmartEnemy(Enemy):
    def collision_distance(self) -> float:
        return 50.


    @property
    def points(self):
        return 10
