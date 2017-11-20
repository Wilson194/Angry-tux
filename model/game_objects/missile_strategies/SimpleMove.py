from model.game_objects.Position import Position
from .MissileStrategy import MissileStrategy


class SimpleMove(MissileStrategy):
    def move(self, gravity: float, position: Position, movement_angle: float, speed: float):
        position.move(movement_angle, 1.)

        return position
