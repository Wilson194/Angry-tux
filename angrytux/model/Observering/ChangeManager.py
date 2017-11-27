from ..Singleton import Singleton


class ChangeManager(metaclass=Singleton):
    def __init__(self):
        self.__observation_map = {}


    def register(self, target: object, observer: object) -> bool:
        if target not in self.__observation_map:
            self.__observation_map[target] = []

        if observer not in self.__observation_map[target]:
            self.__observation_map[target].append(observer)
            return True
        else:
            return False


    def unregister(self, target: object, observer: object) -> bool:
        if target not in self.__observation_map:
            return False

        if observer in self.__observation_map[target]:
            self.__observation_map[target].remove(observer)
            return True
        else:
            return False


    def notify(self, target: object):
        if target not in self.__observation_map:
            return

        for observer in self.__observation_map[target]:
            observer.object_change(target)
