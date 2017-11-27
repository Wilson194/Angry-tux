from angrytux.model.Singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        variables = {}
        exec(open('angrytux/config/Data.py', 'r').read(), variables)

        self.__config = variables['config']


    def __getitem__(self, item):
        if item in self.__config:
            return self.__config.get(item)
        else:
            raise AttributeError('Item {} not found in config!'.format(item))
