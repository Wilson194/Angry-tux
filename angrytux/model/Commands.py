import queue

from angrytux.controller.Commands.Command import Command
from angrytux.controller.Commands.UndoCommand import UndoCommand


class Queue:
    """
    Queue object for commands
    """


    def __init__(self):
        self.__items = []


    def pop(self) -> object:
        """
        Remove top item from queue
        :return: top item of queue
        """
        return self.__items.pop(0)


    def put(self, item: object) -> None:
        """
        Add one item to queue
        :param item: item that you want to put to queue
        """
        self.__items.append(item)


    def empty(self) -> bool:
        """
        Determinate if queue is empty
        :return: True if empty, False otherwise
        """
        return len(self.__items) == 0


class Commands:
    """
    Class that handle behaviour of Commands
    """


    def __init__(self, model):
        self.__queue = Queue()
        self.__stack = queue.LifoQueue()
        self.__model = model


    def add_command(self, command: Command) -> None:
        """
        Add command to queue
        :param command: Command object
        """
        self.__queue.put(command)


    def do_commands(self) -> bool:
        """
        Process all commands in queue
        :return: True, if something happened, False otherwise
        """
        something_happend = False
        while not self.__queue.empty():
            something_happend = True
            command = self.__queue.pop()

            if isinstance(command, UndoCommand):
                if self.__stack.empty():
                    continue
                command = self.__stack.get_nowait()
                command.undo()
            else:
                if command.create_memento:
                    memento = self.__model.create_memento()
                    command.memento = memento

                command.execute()

                self.__stack.put_nowait(command)

        return something_happend
