import pytest

from angrytux.model.game_objects.Obstacle import Obstacle
from angrytux.model.game_objects.Position import Position


@pytest.fixture
def utils():
    return Utils()


@pytest.fixture
def callable_class():
    return CallableClass()


@pytest.fixture
def obstacle():
    return Obstacle(Position(50, 50))


class Utils:
    def compare_rounded_tuple(self, x1, x2):
        for i, j in zip(x1, x2):
            if round(i) != round(j):
                return False

        return True


    def compare_classes(self, class1, class2):
        name1 = type(class1).__name__

        name2 = type(class2).__name__

        return name1 == name2


class CallableClass:
    def __call__(self, *args, **kwargs):
        return self


    def __getattribute__(self, item):
        return self
