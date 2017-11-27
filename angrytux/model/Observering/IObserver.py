from abc import ABC, abstractmethod


class IObserver(ABC):
    @abstractmethod
    def object_change(self, subject):
        pass
