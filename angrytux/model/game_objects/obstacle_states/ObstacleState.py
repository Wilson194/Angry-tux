from abc import ABC, abstractmethod


class ObstacleState(ABC):
    def __init__(self, obstacle):
        self._obstacle = obstacle


    @abstractmethod
    def hit(self):
        pass


    @property
    @abstractmethod
    def delete(self) -> bool:
        pass
