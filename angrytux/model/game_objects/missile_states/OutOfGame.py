from angrytux.model.game_objects.missile_states.MissileState import MissileState


class OutOfGame(MissileState):
    @property
    def delete(self):
        return True
