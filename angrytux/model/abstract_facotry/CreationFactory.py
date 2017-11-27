from angrytux.model.Singleton import Singleton
from .AbstractFactory import AbstractFactory


class CreationFactory(metaclass=Singleton):
    def __init__(self, factory: AbstractFactory = None):
        self.__factory = factory


    @property
    def factory(self):
        return self.__factory


    def __getattr__(self, item):
        return self.__factory.__getattribute__(item)
