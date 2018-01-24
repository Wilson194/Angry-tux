from abc import ABC, abstractmethod


class CannonState(ABC):
    """
    Abstract class for cannon state, defining interface for cannon
    """


    @abstractmethod
    def shoot(self) -> tuple:
        """
        Shoot missile from cannon
        :return: tuple of created missiles
        """
        pass


    @abstractmethod
    def change_state(self) -> None:
        """
        Change state of cannon
        :return: None
        """
        pass


    @property
    @abstractmethod
    def points_multiple(self) -> int:
        """
        Property that determinate, multiple of points when collided with some object
        :return:
        """
        pass


    @property
    @abstractmethod
    def shoot_cost(self) -> int:
        """
        Property that determinate point cost of one shoot
        :return:
        """
        pass
