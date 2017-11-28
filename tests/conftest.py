import pytest


@pytest.fixture
def utils():
    return Utils()


@pytest.fixture
def callable_class():
    return CallableClass()


class Utils:
    def compare_rounded_tuple(self, x1, x2):
        for i, j in zip(x1, x2):
            if round(i) != round(j):
                return False

        return True


class CallableClass:
    def __call__(self, *args, **kwargs):
        return self


    def __getattribute__(self, item):
        return self
