from angrytux.controller.Commands.Command import Command


class CannonStrengthUpCommand(Command):
    """
    Command for increase cannon shoot strength
    """


    @property
    def create_memento(self):
        return False


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def execute(self):
        self.__proxy.change_strength(0.3)


    def undo(self):
        self.__proxy.change_strength(-0.3)


    def __repr__(self):
        return "<Command> Cannon strength up"
