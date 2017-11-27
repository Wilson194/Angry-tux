import queue

from angrytux.controller.Commands.UndoCommand import UndoCommand


class Queue:
    def __init__(self):
        self.__items = []


    def pop(self):
        return self.__items.pop(0)


    def put(self, item):
        self.__items.append(item)


    def empty(self):
        return len(self.__items) == 0


class Commands:
    def __init__(self, model):
        self.__queue = Queue()
        self.__stack = queue.LifoQueue()
        self.__model = model


    def add_command(self, command):
        self.__queue.put(command)


    def do_commands(self):
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
