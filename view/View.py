import pygame
import os
from model.GameModel import GameModel
from model.Observering.ChangeManager import ChangeManager
from model.Observering.IObserver import IObserver
from model.Visitor.IVisitor import IVisitor
from model.game_objects.Cannon import Cannon
from model.game_objects.Enemy import Enemy
from model.game_objects.Missile import Missile
from model.game_objects.Obstacle import Obstacle
from view.ImageLoader import ImageLoader


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

        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Angry tux')
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = pygame.time.Clock()
        self.__screen.fill((255, 255, 255))

        pygame.display.update()


    def _visit_obstacle(self, obstacle: Obstacle):
        pass


    def _visit_missile(self, missile: Missile):
        pass


    def _visit_enemy(self, enemy: Enemy):
        pass


    def _visit_cannon(self, canon: Cannon):
        x = canon.position.x_position
        y = canon.position.y_position
        angle = canon.shooting_angle

        cannon_img = self.__imageLoader.get_cannon()
        img, rect = rot_center(cannon_img, (x + 59, y + 75), angle)
        self.__screen.blit(img, rect)

        wheel_img = self.__imageLoader.get_wheel()
        self.__screen.blit(wheel_img, (x + 40, y + 65))


def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect)
    return rot_image, rot_rect
