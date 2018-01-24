from angrytux.controller.Commands.Command import Command
from angrytux.proxy.Proxy import Proxy


class CannonAngleUpCommand(Command):
    """
    Command for rise cannon shooting angle
    """


    @property
    def create_memento(self) -> bool:
        return False


    def __init__(self, proxy: Proxy) -> None:
        super().__init__()
        self.__proxy = proxy


    def undo(self) -> None:
        self.__proxy.angle_cannon(-5)


    def execute(self) -> None:
        self.__proxy.angle_cannon(5)


    def __repr__(self) -> str:
        return '<Command> Cannon angle move up'
