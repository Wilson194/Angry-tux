from angrytux.controller.Commands.Command import Command


class UndoCommand(Command):
    """
    Command for undo process
    """


    def execute(self) -> None:
        pass


    def undo(self) -> None:
        pass


    @property
    def create_memento(self) -> bool:
        return False
