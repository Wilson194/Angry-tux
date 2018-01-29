from angrytux.view.ImageLoader import ImageLoader
import angrytux.view.ImageLoader
import pytest


class CounterClass:
    def __init__(self):
        self.counter = 0


    def call_counter(self, *args, **argv):
        self.counter += 1
        return self.counter


@pytest.mark.parametrize('image_name', (
        'get_tux',
        'get_cannon',
        'get_wheel',
        'get_vista',
        'get_win_10',
        'get_win_98',
        'get_blue_dead',
        'get_wall',
        'get_tux_small',
        'get_background'))
def test_image_loader_and_caching_images(monkeypatch, image_name):
    image_loader = ImageLoader()
    counter_class = CounterClass()

    monkeypatch.setattr(angrytux.view.ImageLoader, 'load_image', counter_class.call_counter)

    assert getattr(image_loader, image_name)()[1] == 1
    assert getattr(image_loader, image_name)()[1] == 1
