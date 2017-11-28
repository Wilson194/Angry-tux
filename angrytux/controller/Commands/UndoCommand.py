from angrytux.controller.Commands.Command import Command


class UndoCommand(Command):
    """
    Command for undo process
    """


    def execute(self):
        pass


    def undo(self):
        pass


    @property
    def create_memento(self):
        return False
