from abc import ABC, abstractmethod


class CannonState(ABC):
    @abstractmethod
    def shoot(self) -> tuple:
        pass


    @abstractmethod
    def change_state(self):
        pass


    @property
    @abstractmethod
    def points_multiple(self) -> int:
        pass


    @property
    @abstractmethod
    def shoot_cost(self) -> int:
        pass
