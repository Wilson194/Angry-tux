from angrytux.controller.Commands.Command import Command


class CannonStrengthDownCommand(Command):
    """
    Command for decrease cannon shoot strength
    """


    @property
    def create_memento(self):
        return False


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def execute(self):
        self.__proxy.change_strength(-0.3)


    def undo(self):
        self.__proxy.change_strength(0.3)


    def __repr__(self):
        return "<Command> Cannon strength down"
