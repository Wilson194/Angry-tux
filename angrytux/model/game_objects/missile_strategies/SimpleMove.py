from angrytux.model.game_objects.Missile import Missile
from .MissileStrategy import MissileStrategy


class SimpleMove(MissileStrategy):
    def move(self, missile: Missile, gravity: float):
        missile.movement_angle = missile.movement_angle if missile.movement_angle < -90 else missile.movement_angle - 9.81 / 20
        missile.position.move(missile.movement_angle, missile.speed)