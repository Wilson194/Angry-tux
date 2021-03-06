import pygame
from angrytux.config.Config import Config
from angrytux.model.GameModel import GameModel
from angrytux.model.Observering.ChangeManager import ChangeManager
from angrytux.model.Observering.IObserver import IObserver
from angrytux.model.Visitor.IVisitor import IVisitor
from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Obstacle import Obstacle
from angrytux.model.game_objects.cannon_states.CannonState import CannonState
from angrytux.model.game_objects.enemies.DummyEnemy import DummyEnemy
from angrytux.model.game_objects.enemies.Enemy import Enemy
from angrytux.model.game_objects.enemies.MovingEnemy import MovingEnemy
from angrytux.model.game_objects.enemies.SmartEnemy import SmartEnemy
from angrytux.model.game_objects.enemies.enemy_states.HittedState import HittedState
from angrytux.view.ImageLoader import ImageLoader

from angrytux.model.game_objects.Cannon import Cannon
from angrytux.view.ProgressBar import ProgressBar


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

        self.__font = pygame.font.SysFont("comicsansms", 20)
        self.__big_font = pygame.font.SysFont("comicsansms", 30)


    def object_change(self, subject) -> None:
        """
        Redraw all items in game
        :param subject: subject of observer pattern
        """

        self._draw_background()
        all_objects = self.__model.get_all_game_objects()
        # self.__screen.fill((255, 255, 255))
        for obj in all_objects:
            obj.accept(self)

        self._draw_score(self.__model.score)
        self._draw_shoot_state(self.__model.cannon.state)
        self._draw_gravity_value(self.__model.gravity)

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


    def _visit_obstacle(self, obstacle: Obstacle) -> None:
        """
        Visit object for visitor pattern
        :param obstacle: obstacle object
        """
        size, tux_img = self.__imageLoader.get_wall()
        x = obstacle.position.x_position - size[0] / 2
        y = obstacle.position.y_position - size[1] / 2

        self.__screen.blit(tux_img, (x, y))


    def _visit_missile(self, missile: Missile) -> None:
        """
        Visit missile for visitor pattern
        :param missile: missile object
        """
        size, tux_img = self.__imageLoader.get_tux()
        x = missile.position.x_position - size[0] / 2
        y = missile.position.y_position - size[1] / 2

        self.__screen.blit(tux_img, (x, y))


    def _visit_enemy(self, enemy: Enemy) -> None:
        """
        Visit enemy for visitor pattern
        :param enemy: enemy object
        """
        if isinstance(enemy.state, HittedState):
            size, img = self.__imageLoader.get_blue_dead()
        else:
            if isinstance(enemy, DummyEnemy):
                size, img = self.__imageLoader.get_vista()
            if isinstance(enemy, SmartEnemy):
                size, img = self.__imageLoader.get_win_10()
            if isinstance(enemy, MovingEnemy):
                size, img = self.__imageLoader.get_win_98()

        x = enemy.position.x_position - size[0] / 2
        y = enemy.position.y_position - size[1] / 2
        self.__screen.blit(img, (x, y))


    def _visit_cannon(self, canon: Cannon) -> None:
        """
        Visit cannon for visitor pattern
        :param canon: cannon object
        """
        x = canon.position.x_position
        y = canon.position.y_position
        angle = canon.shooting_angle

        size, cannon_img = self.__imageLoader.get_cannon()
        img, rect = rot_center(cannon_img, (x + 59, y + 75), angle - 15)
        self.__screen.blit(img, rect)

        size, wheel_img = self.__imageLoader.get_wheel()
        self.__screen.blit(wheel_img, (x + 40, y + 65))

        self._draw_strength_bar(canon.strength)


    def _draw_strength_bar(self, strength: float) -> None:
        """
        Draw strength bar at top of window
        :param strength: value of strength
        """
        p = ProgressBar(self.__screen, 230, 10, 150, 20, 'Strength', self.__font)
        p.update(strength)


    def _draw_score(self, score: int) -> None:
        """
        Draw score text at top of windows
        :param score: actual score value
        """
        text_surface = self.__big_font.render('Score: {}'.format(score), False, (0, 0, 0))
        self.__screen.blit(text_surface, (400, 10))


    def _draw_shoot_state(self, state: CannonState) -> None:
        """
        Draw shoot state (one or two tux at top of windows
        :param state: State of cannon
        """
        size, tux_img = self.__imageLoader.get_tux_small()
        text_surface = self.__big_font.render('Shoot: ', False, (0, 0, 0))

        self.__screen.blit(text_surface, (600, 10))

        if state == 'SingleShoot':
            self.__screen.blit(tux_img, (670, 10))

        if state == 'DoubleShoot':
            self.__screen.blit(tux_img, (670, 10))
            self.__screen.blit(tux_img, (690, 10))


    def _draw_gravity_value(self, gravity: float) -> None:
        """
        Draw gravity value, text at top window
        :param gravity: current gravity value
        """
        text_surface = self.__big_font.render('Gravity: {:.2f}'.format(gravity), False, (0, 0, 0))
        self.__screen.blit(text_surface, (50, 10))


    def _draw_background(self) -> None:
        """
        Draw background of game
        """
        size, bg = self.__imageLoader.get_background()
        bg.convert_alpha()

        self.__screen.blit(bg, pygame.rect.Rect(0, 0, 500, 500))


def rot_center(image, rect: tuple, angle: float) -> tuple:
    """
    rotate an image while keeping its center
    :param image: image object for rotating
    :param rect: current position rectangle
    :param angle: rotation angle
    :return: tuple of image and rectangle objects
    """
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect)
    return rot_image, rot_rect
