import pygame

from config.Config import Config
from model.GameModel import GameModel
from model.Observering.ChangeManager import ChangeManager
from model.Observering.IObserver import IObserver
from model.Visitor.IVisitor import IVisitor
from model.game_objects.Cannon import Cannon
from model.game_objects.Missile import Missile
from model.game_objects.Obstacle import Obstacle
from model.game_objects.enemies.DumpEnemy import DumpEnemy
from model.game_objects.enemies.Enemy import Enemy
from model.game_objects.enemies.enemy_states.HittedState import HittedState
from view.ImageLoader import ImageLoader
from view.ProgressBar import ProgressBar


class View(IObserver, IVisitor):
    """
    Base view class, drawing all object and manage game window
    """


    def __init__(self):
        self.__screen = None
        self.__clock = None
        self.__imageLoader = ImageLoader()
        self.__model = GameModel()

        self.__change_manager = ChangeManager()

        self.__change_manager.register(self.__model, self)


    def object_change(self, subject):
        all_objects = self.__model.get_all_game_objects()
        self.__screen.fill((255, 255, 255))
        for obj in all_objects:
            obj.accept(self)
        pygame.display.flip()


    def initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """
        # result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Angry tux')
        self.__screen = pygame.display.set_mode(Config()['windows_size'])
        self.__clock = pygame.time.Clock()
        self.__screen.fill((255, 255, 255))

        pygame.display.update()


    def _visit_obstacle(self, obstacle: Obstacle):
        pass


    def _visit_missile(self, missile: Missile):
        size, tux_img = self.__imageLoader.get_tux()
        x = missile.position.x_position - size[0] / 2
        y = missile.position.y_position - size[1] / 2

        self.__screen.blit(tux_img, (x, y))


    def _visit_enemy(self, enemy: Enemy):
        if isinstance(enemy, DumpEnemy):
            if isinstance(enemy.state, HittedState):
                size, img = self.__imageLoader.get_blue_dead()
            else:
                size, img = self.__imageLoader.get_vista()

        x = enemy.position.x_position - size[0] / 2
        y = enemy.position.y_position - size[1] / 2
        self.__screen.blit(img, (x, y))


    def _visit_cannon(self, canon: Cannon):
        x = canon.position.x_position
        y = canon.position.y_position
        angle = canon.shooting_angle

        size, cannon_img = self.__imageLoader.get_cannon()
        img, rect = rot_center(cannon_img, (x + 59, y + 75), angle)
        self.__screen.blit(img, rect)

        size, wheel_img = self.__imageLoader.get_wheel()
        self.__screen.blit(wheel_img, (x + 40, y + 65))

        self._draw_strength_bar(canon.strength)


    def _draw_strength_bar(self, strength):
        p = ProgressBar(self.__screen, 200, 10, 150, 20, 'Strength', pygame.font.SysFont("comicsansms", 20))
        p.update(strength)


def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect)
    return rot_image, rot_rect
