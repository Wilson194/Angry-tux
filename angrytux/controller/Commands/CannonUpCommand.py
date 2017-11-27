from angrytux.controller.Commands.Command import Command


class CannonUpCommand(Command):
    """
    Command for cannon move up
    """


    @property
    def create_memento(self):
        return False


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def undo(self):
        self.__proxy.move_cannon(-90, 5)


    def execute(self):
        self.__proxy.move_cannon(90, 5)


    def __repr__(self):
        return '<Command> Cannon move up'
