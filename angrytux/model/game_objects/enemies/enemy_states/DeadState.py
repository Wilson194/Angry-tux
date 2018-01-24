from angrytux.model.game_objects.enemies.enemy_states.EnemyState import EnemyState


class DeadState(EnemyState):
    @property
    def collidable(self) -> bool:
        """
        Determinate if this object could collied with missile
        :return: True if collide, False otherwise
        """
        return False


    def hit(self) -> None:
        """
        Method for hit this enemy (what to do when hitted)
        Do nothing
        """
        pass


    def move(self) -> bool:
        """
        No moving for this state
        :return: False
        """
        return False


    @property
    def delete(self) -> bool:
        return True
