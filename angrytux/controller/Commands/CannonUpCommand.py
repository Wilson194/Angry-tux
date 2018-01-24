from angrytux.controller.Commands.Command import Command


class CannonUpCommand(Command):
    """
    Command for cannon move up
    """


    @property
    def create_memento(self) -> bool:
        return False


    def __init__(self, proxy) -> None:
        super().__init__()
        self.__proxy = proxy


    def undo(self) -> None:
        self.__proxy.move_cannon(-90, 5)


    def execute(self) -> None:
        self.__proxy.move_cannon(90, 5)


    def __repr__(self) -> str:
        return '<Command> Cannon move up'
