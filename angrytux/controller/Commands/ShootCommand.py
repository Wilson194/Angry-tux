from angrytux.controller.Commands.Command import Command
from angrytux.proxy.Proxy import Proxy


class ShootCommand(Command):
    """
    Command for cannon shoot
    """


    @property
    def create_memento(self) -> bool:
        return True


    def __init__(self, proxy: Proxy) -> None:
        super().__init__()
        self.__proxy = proxy


    def undo(self) -> None:
        self.__proxy.load_memento(self.memento)


    def execute(self) -> None:
        self.__proxy.shoot()


    def __repr__(self) -> str:
        return '<Command> Shoot'
