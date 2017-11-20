from model.game_objects.missile_states.MissileState import MissileState


class Flying(MissileState):
    @property
    def delete(self):
        return False
