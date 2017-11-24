from controller.Commands.Command import Command


class ShootCommand(Command):
    """
    Command for cannon move up
    """


    @property
    def create_memento(self):
        return True


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def undo(self):
        self.__proxy.load_memento(self.memento)


    def execute(self):
        self.__proxy.shoot()


    def __repr__(self):
        return '<Command> Shoot'
