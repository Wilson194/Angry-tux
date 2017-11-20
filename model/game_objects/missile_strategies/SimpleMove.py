from .MissileStrategy import MissileStrategy


class SimpleMove(MissileStrategy):
    def move(self, gravity, position):
        position.move()
