from controller.Commands.Command import Command


class CannonAngleUpCommand(Command):
    """
    Command for cannon move down
    """


    @property
    def create_memento(self):
        return False


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def undo(self):
        self.__proxy.angle_cannon(-5)


    def execute(self):
        self.__proxy.angle_cannon(5)


    def __repr__(self):
        return '<Command> Cannon angle move up'
