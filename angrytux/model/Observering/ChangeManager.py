from ..Singleton import Singleton


class ChangeManager(metaclass=Singleton):
    """
    Change manager is class for managing observer pattern.
    This class register and unregister all observers and objects and notifying all objects
    """


    def __init__(self):
        self.__observation_map = {}


    def register(self, target: object, observer: object) -> bool:
        """
        Register new observer for target object
        :param target: target object which will be observed
        :param observer: object that observer target
        :return: True if added to list, False otherwise
        """
        if target not in self.__observation_map:
            self.__observation_map[target] = []

        if observer not in self.__observation_map[target]:
            self.__observation_map[target].append(observer)
            return True
        else:
            return False


    def unregister(self, target: object, observer: object) -> bool:
        """
        Unregister observer from list
        :param target: observered target
        :param observer: observer object
        :return: True if removed, False if not found
        """
        if target not in self.__observation_map:
            return False

        if observer in self.__observation_map[target]:
            self.__observation_map[target].remove(observer)
            return True
        else:
            return False


    def notify(self, target: object) -> None:
        """
        Notify all observers, that object changed
        :param target: target object which change
        :return: None
        """
        if target not in self.__observation_map:
            return

        for observer in self.__observation_map[target]:
            observer.object_change(target)
