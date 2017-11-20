from controller.Commands.Command import Command


class CannonStrengthDownCommand(Command):
    def __init__(self, proxy):
        self.__proxy = proxy


    def execute(self):
        self.__proxy.change_strength(-0.3)


    def undo(self):
        self.__proxy.change_strength(0.3)


    def __repr__(self):
        return "<Command> Cannon strength down"
