from controller.Commands.Command import Command


class ShootCommand(Command):
    """
    Command for cannon move up
    """


    def __init__(self, proxy):
        self.__proxy = proxy


    def undo(self):
        pass


    def execute(self):
        self.__proxy.shoot()


    def __repr__(self):
        return '<Command> Shoot'
