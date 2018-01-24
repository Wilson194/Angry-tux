from angrytux.proxy.Proxy import Proxy
from .Command import Command


class ChangeCannonStateCommand(Command):
    """
    Command for change state of cannon
    """


    @property
    def create_memento(self) -> bool:
        return False


    def __init__(self, proxy: Proxy) -> None:
        super().__init__()
        self.__proxy = proxy


    def undo(self) -> None:
        self.__proxy.change_cannon_state()


    def execute(self) -> None:
        self.__proxy.change_cannon_state()


    def __repr__(self) -> str:
        return '<Command> Change state of cannon'
