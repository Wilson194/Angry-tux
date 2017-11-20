from controller.Commands.Command import Command


class QuitCommand(Command):
    """
    Command for quit application
    """


    def undo(self):
        pass


    def execute(self):
        quit(3)


    def __repr__(self):
        return '<Command> Quit application'
