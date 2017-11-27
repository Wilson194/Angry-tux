from angrytux.model.Singleton import Singleton

from angrytux.model.GameModel import GameModel


class Proxy(metaclass=Singleton):
    """
    Proxy between controller and model, Logging all actions
    """

    class ProxyCaller:
        def __init__(self, model, method):
            self.__method = method
            self.__model = model


        def __call__(self, *args, **kwargs):
            if len(args) > 0:
                print(str(args[0]))
            getattr(self.__model, self.__method)(*args, **kwargs)

    def __init__(self):
        self.__model = GameModel()


    def __getattr__(self, item):
        return self.ProxyCaller(self.__model, item)
