from abc import ABC, abstractmethod


class ObstacleState(ABC):
    """
    Interface for obstacle states
    """


    def __init__(self, obstacle):
        self._obstacle = obstacle


    @abstractmethod
    def hit(self) -> None:
        """
        What obstacle should do after being hit by missile
        """
        pass


    @property
    @abstractmethod
    def delete(self) -> bool:
        """
        Determinate, if obstacle in this state should be deleted by garbage collector
        :return: True for delete, False otherwise
        """
        pass
