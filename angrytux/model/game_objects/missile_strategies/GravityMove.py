from angrytux.model.game_objects.Missile import Missile
from .MissileStrategy import MissileStrategy


class GravityMove(MissileStrategy):
    """
    Moving with gravity and simple model of balistic curve
    """


    def move(self, missile: Missile, gravity: float) -> None:
        """
        Move depends on angle, speed and gravity.
        This move try to be same like real moving
        :param missile: Missile object
        :param gravity: actual value of gravity
        """
        if missile.movement_angle > 0:
            missile.speed -= gravity * 0.002
        else:
            missile.speed += gravity * 0.003

        if missile.speed < 1:
            missile.movement_angle = -25

        missile.movement_angle = missile.movement_angle if missile.movement_angle < -90 else missile.movement_angle - gravity / 20

        missile.position.move(missile.movement_angle, missile.speed)
