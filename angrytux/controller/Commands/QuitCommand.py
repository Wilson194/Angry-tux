from angrytux.controller.Commands.Command import Command


class QuitCommand(Command):
    """
    Command for quit application
    """


    @property
    def create_memento(self) -> bool:
        return False


    def undo(self) -> None:
        pass


    def execute(self) -> None:
        quit(3)


    def __repr__(self) -> str:
        return '<Command> Quit application'
