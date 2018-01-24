from abc import ABC, abstractmethod

from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Obstacle import Obstacle
from angrytux.model.game_objects.enemies.Enemy import Enemy

from angrytux.model.game_objects.Cannon import Cannon


class IVisitor(ABC):
    """
    Abstract interface for visitor pattern
    """


    def visit(self, visited_object):
        """
        Determinate visit function called
        :param visited_object:
        :return:
        """
        if str(visited_object) == 'Cannon':
            self._visit_cannon(visited_object)
        elif str(visited_object) == 'Missile':
            self._visit_missile(visited_object)
        elif str(visited_object) == 'Enemy':
            self._visit_enemy(visited_object)
        elif str(visited_object) == 'Obstacle':
            self._visit_obstacle(visited_object)


    @abstractmethod
    def _visit_cannon(self, canon: Cannon):
        """
        Visit cannon object
        :param canon: Cannon object
        """
        pass


    @abstractmethod
    def _visit_missile(self, missile: Missile):
        """
        Visit missile object
        :param missile: Missile object
        """
        pass


    @abstractmethod
    def _visit_enemy(self, enemy: Enemy):
        """
        Visit enemy object
        :param enemy: Enemy object
        """
        pass


    @abstractmethod
    def _visit_obstacle(self, obstacle: Obstacle):
        """
        Visit obstacle object
        :param obstacle: Obstacle object
        """
        pass
