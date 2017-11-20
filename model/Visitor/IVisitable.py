from abc import ABC, abstractmethod


class IVisitable(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
