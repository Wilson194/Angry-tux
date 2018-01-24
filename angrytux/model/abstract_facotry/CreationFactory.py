from angrytux.model.Singleton import Singleton
from .AbstractFactory import AbstractFactory


class CreationFactory(metaclass=Singleton):
    """
    Creating factory is singleton, which hold selected AbstractFactory
    Just delegate functions to correct abstract factory
    """


    def __init__(self, factory: AbstractFactory = None):
        self.__factory = factory


    @property
    def factory(self) -> AbstractFactory:
        """
        Getter for selected factory
        :return: Specific factory
        """
        return self.__factory


    def __getattr__(self, item):
        return self.__factory.__getattribute__(item)
