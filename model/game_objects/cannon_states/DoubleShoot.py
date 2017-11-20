from model.game_objects.cannon_states.CannonState import CannonState


class DoubleShoot(CannonState):
    def __init__(self, cannon):
        self.__cannon = cannon


    def shoot(self):
        pass
