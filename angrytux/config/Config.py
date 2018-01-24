import os

from angrytux.model.Singleton import Singleton


class Config(metaclass=Singleton):
    """
    Class for global game config
    Has getitem from getting variables
    Singleton class
    """


    def __init__(self):
        variables = {}
        exec(open(os.path.join(os.path.dirname(__file__), 'Data.py'), 'r').read(), variables)

        self.__config = variables['config']


    def __getitem__(self, item):
        if item in self.__config:
            return self.__config.get(item)
        else:
            raise AttributeError('Item {} not found in config!'.format(item))
