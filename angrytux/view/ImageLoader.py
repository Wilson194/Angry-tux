import os

import pygame

from angrytux.config.Config import Config

IMAGES_PATH = os.path.join('angrytux', 'resources', 'images')


def load_image(image, size):
    tux = pygame.image.load(os.path.join(IMAGES_PATH, image))
    tux = pygame.transform.scale(tux, size)

    return tux


class ImageLoader:
    def __init__(self):
        self.__loaded = {}


    def __return_cached(self, name, image_name, size):
        if name not in self.__loaded:
            image = load_image(image_name, size)
            self.__loaded[name] = image

        return self.__loaded[name]


    def get_tux(self):
        size = (30, 30)
        image_name = 'tux_circle.png'

        return size, self.__return_cached('tux', image_name, size)


    def get_cannon(self):
        size = (125, 125)
        image_name = 'cannon.png'

        return size, self.__return_cached('cannon', image_name, size)


    def get_wheel(self):
        size = (40, 40)
        image_name = 'wheel.png'

        return size, self.__return_cached('wheel', image_name, size)


    def get_vista(self):
        size = (60, 60)
        image_name = 'vista.png'

        return size, self.__return_cached('vista', image_name, size)


    def get_win_10(self):
        size = (60, 60)
        image_name = 'windows_10.png'

        return size, self.__return_cached('win10', image_name, size)


    def get_win_98(self):
        size = (60, 60)
        image_name = 'windows_98.png'

        return size, self.__return_cached('win98', image_name, size)


    def get_blue_dead(self):
        size = (40, 40)

        image_name = 'blue_dead.jpg'
        return size, self.__return_cached('blue_dead', image_name, size)


    def get_wall(self):
        size = (60, 60)
        image_name = 'firewall.png'

        return size, self.__return_cached('firewall', image_name, size)


    def get_tux_small(self):
        size = (20, 20)
        image_name = 'tux_circle.png'

        return size, self.__return_cached('tux_small', image_name, size)


    def get_background(self):
        size = Config()['windows_size']
        image_name = 'background.jpg'

        return size, self.__return_cached('background', image_name, size)
