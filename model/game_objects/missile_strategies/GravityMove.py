from model.game_objects.Missile import Missile
from .MissileStrategy import MissileStrategy


class GravityMove(MissileStrategy):
    def move(self, missile: Missile, gravity: float):
        if missile.movement_angle > 0:
            missile.speed -= 0.02
        else:
            missile.speed += 0.03

        if missile.speed < 0.1:
            missile.movement_angle = -5

        missile.movement_angle = missile.movement_angle if missile.movement_angle < -90 else missile.movement_angle - gravity / 20

        missile.position.move(missile.movement_angle, missile.speed)
