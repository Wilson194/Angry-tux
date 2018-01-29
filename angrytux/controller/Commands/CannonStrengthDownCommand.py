from angrytux.controller.Commands.Command import Command
from angrytux.proxy.Proxy import Proxy


class CannonStrengthDownCommand(Command):
    """
    Command for decrease cannon shoot strength
    """


    @property
    def create_memento(self) -> bool:
        return False


    def __init__(self, proxy: Proxy):
        super().__init__()
        self.__proxy = proxy


    def execute(self) -> None:
        self.__proxy.change_strength(-0.3)


    def undo(self) -> None:
        self.__proxy.change_strength(0.3)


    def __repr__(self) -> str:
        return "<Command> Cannon strength down"
