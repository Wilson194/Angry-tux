from angrytux.controller.Commands.Command import Command
from angrytux.proxy.Proxy import Proxy


class GravityDownCommand(Command):
    """
    Command for decrease gravity of game
    """


    def __init__(self, proxy: Proxy) -> None:
        super().__init__()
        self.__proxy = proxy


    def execute(self) -> None:
        self.__proxy.change_gravity(-0.5)


    @property
    def create_memento(self) -> bool:
        return False


    def undo(self) -> None:
        self.__proxy.change_gravity(0.5)


    def __repr__(self) -> str:
        return '<Command> Command for decrease gravity'
