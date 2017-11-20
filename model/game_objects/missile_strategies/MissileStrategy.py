from abc import ABC, abstractmethod


class MissileStrategy(ABC):
    @abstractmethod
    def move(self, gravity, position):
        pass
