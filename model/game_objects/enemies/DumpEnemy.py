from model.game_objects.enemies.Enemy import Enemy


class DumpEnemy(Enemy):
    def collision_distance(self) -> float:
        return 40


    @property
    def points(self):
        return 10
