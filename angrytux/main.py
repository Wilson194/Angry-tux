import pygame
from angrytux.config.Config import Config
from angrytux.controller.Keyboard import Keyboard
from angrytux.model.GameModel import GameModel
from angrytux.model.Levels.Level1Creator import Level1Creator
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.abstract_facotry.RealisticFactory import RealisticFactory

from angrytux.view.View import View


def run():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    pygame.key.set_repeat(300, 40)

    controller = Keyboard()

    view = View()
    view.initialize()

    CreationFactory(RealisticFactory())

    model = GameModel()
    model.model_builder(Level1Creator())

    clock = pygame.time.Clock()
    while 1:
        model.tick()
        controller.tick()
        clock.tick(Config()['fps']) / 1000


if __name__ == '__main__':
    run()
