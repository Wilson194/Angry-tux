from angrytux.model.game_objects.missile_states.MissileState import MissileState


class Collided(MissileState):
    @property
    def delete(self):
        return True
