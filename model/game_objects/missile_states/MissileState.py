from abc import ABC, abstractmethod


class MissileState(ABC):
    @property
    @abstractmethod
    def delete(self):
        pass
