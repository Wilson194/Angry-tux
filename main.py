from config.Config import Config
from controller.Keyboard import Keyboard
from model.GameModel import GameModel
from model.abstract_facotry.CreationFactory import CreationFactory
from model.abstract_facotry.SimpleFactory import SimpleFactory
from proxy.Proxy import Proxy
from view.View import View
import pygame


def run():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    pygame.key.set_repeat(300, 40)

    controller = Keyboard()

    view = View()
    view.initialize()

    CreationFactory(SimpleFactory())

    model = GameModel()

    clock = pygame.time.Clock()
    while 1:
        model.tick()
        controller.tick()
        clock.tick(Config()['fps']) / 1000


if __name__ == '__main__':
    run()
