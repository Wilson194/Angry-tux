from abc import ABC, abstractmethod


class CannonState(ABC):
    @abstractmethod
    def shoot(self) -> tuple:
        pass
