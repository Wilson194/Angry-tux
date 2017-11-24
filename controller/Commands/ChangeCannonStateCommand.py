from .Command import Command


class ChangeCannonStateCommand(Command):
    @property
    def create_memento(self):
        return False


    def __init__(self, proxy):
        super().__init__()
        self.__proxy = proxy


    def undo(self):
        self.__proxy.change_cannon_state()


    def execute(self):
        self.__proxy.change_cannon_state()


    def __repr__(self):
        return '<Command> Change state of cannon'
