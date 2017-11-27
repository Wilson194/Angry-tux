from angrytux.controller.Commands.Command import Command


class GravityUpCommand(Command):
    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def execute(self):
        self.__proxy.change_gravity(0.5)


    @property
    def create_memento(self):
        return False


    def undo(self):
        self.__proxy.change_gravity(-0.5)
