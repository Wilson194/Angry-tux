from angrytux.controller.Commands.Command import Command


class CannonStrengthUpCommand(Command):
    """
    Command for increase cannon shoot strength
    """


    @property
    def create_memento(self) -> bool:
        return False


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def execute(self) -> None:
        self.__proxy.change_strength(0.3)


    def undo(self) -> None:
        self.__proxy.change_strength(-0.3)


    def __repr__(self) -> str:
        return "<Command> Cannon strength up"
