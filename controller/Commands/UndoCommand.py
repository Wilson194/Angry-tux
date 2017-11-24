from controller.Commands.Command import Command


class UndoCommand(Command):
    def execute(self):
        pass


    def undo(self):
        pass


    @property
    def create_memento(self):
        return False
