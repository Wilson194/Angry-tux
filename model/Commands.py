from model import Singleton
import queue


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
    def __init__(self):
        self.__queue = Queue()
        self.__stack = queue.LifoQueue()


    def add_command(self, command):
        self.__queue.put(command)


    def do_commands(self):
        something_happend = False
        while not self.__queue.empty():
            something_happend = True
            command = self.__queue.pop()
            command.execute()

        return something_happend
