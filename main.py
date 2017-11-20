from controller.Keyboard import Keyboard
from model.GameModel import GameModel
from model.abstract_facotry.CreationFactory import CreationFactory
from model.abstract_facotry.SimpleFactory import SimpleFactory
from proxy.Proxy import Proxy
from view.View import View


def run():
    controller = Keyboard()

    view = View()
    view.initialize()

    CreationFactory(SimpleFactory())

    model = GameModel()

    while 1:
        model.tick()
        controller.tick()


if __name__ == '__main__':
    run()
