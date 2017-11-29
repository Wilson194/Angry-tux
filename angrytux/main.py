import os
import pygame
import argparse
from angrytux.config.Config import Config
from angrytux.controller.Keyboard import Keyboard
from angrytux.model.GameModel import GameModel
from angrytux.model.Levels.Level1Creator import Level1Creator
from angrytux.model.Levels.Level2Creator import Level2Creator
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.abstract_facotry.RealisticFactory import RealisticFactory
from angrytux.model.abstract_facotry.SimpleFactory import SimpleFactory

from angrytux.view.View import View

ROOT_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')


def run():
    parser = argparse.ArgumentParser(description='AngryTux game')
    parser.add_argument('-l', '--level', dest='level', action='store',
                        default=1, help='Set play level')
    parser.add_argument('-f', '--factory', dest='factory', action='store',
                        default='simple', help='Set creation factory (simple/realistic)')

    args = parser.parse_args()

    # init pygame
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.init()
    pygame.init()
    pygame.key.set_repeat(300, 40)

    # Init controller
    controller = Keyboard()

    # Init view
    view = View()
    view.initialize()

    if args.factory == 'simple':
        CreationFactory(SimpleFactory())
    elif args.factory == 'realistic':
        CreationFactory(RealisticFactory())
    else:
        print('Please use only simple or realistic mode, if you want some more, you can create it')
        quit(10)

    # Init model
    model = GameModel()

    if int(args.level) == 1:
        model.model_builder(Level1Creator())
    elif int(args.level) == 2:
        model.model_builder(Level2Creator())
    else:
        print('Only 1 and 2 level is complete, you can create some more!')
        quit(10)

    clock = pygame.time.Clock()
    while 1:
        model.tick()
        controller.tick()
        clock.tick(Config()['fps']) / 1000


if __name__ == '__main__':
    run()
