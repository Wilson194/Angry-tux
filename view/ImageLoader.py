import os
import pygame

IMAGES_PATH = os.path.join('resources', 'images')


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
        size = (80, 150)
        image_name = 'tux.png'

        return self.__return_cached('tux', image_name, size)


    def get_cannon(self):
        size = (125, 125)
        image_name = 'cannon.png'

        return self.__return_cached('cannon', image_name, size)


    def get_wheel(self):
        size = (40, 40)
        image_name = 'wheel.png'

        return self.__return_cached('wheel', image_name, size)
