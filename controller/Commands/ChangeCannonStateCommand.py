from .Command import Command


class ChangeCannonStateCommand(Command):
    def __init__(self, proxy):
        self.__proxy = proxy


    def undo(self):
        self.__proxy.change_cannon_state()


    def execute(self):
        self.__proxy.change_cannon_state()


    def __repr__(self):
        return '<Command> Change state of cannon'
