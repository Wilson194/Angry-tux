import pygame

from angrytux.config.Config import Config

MIN_PROGRESS = 10
MAX_PROGRESS = 100


def rescale(number: float) -> float:
    """
    Rescale size of progress bar
    :param number:
    :return:
    """
    result = (((MAX_PROGRESS - MIN_PROGRESS) * (number - Config()['cannon_min_strength'])) / (
        Config()['cannon_max_strength'] - Config()['cannon_min_strength'])) + MIN_PROGRESS

    return result


class ProgressBar:
    """
    Class for progress bar
    """


    def __init__(self, screen, x, y, bar_width, bar_height, name, font):
        self.screen = screen
        self.color = (102, 170, 255)
        self.bgcolor = (255, 255, 255)
        self.txt_color = (0, 0, 0)
        self.x = x
        self.y = y
        self.width = bar_width
        self.height = bar_height
        self.font = font
        self.text_size = self.font.size(name)
        self.text = self.font.render(name, True, self.txt_color)
        self.bar_space = pygame.Surface((self.width, self.height))
        self.bar_space.fill(self.bgcolor)
        self.bar = pygame.Surface((self.width, self.height))


    def update(self, value: float) -> None:
        """
        Update size of bar
        :param value: value of bar in percentage
        """
        percent = rescale(value)
        pygame.draw.rect(self.bar, self.color, (0, 0, self.width, self.height), 2)
        self.bar = pygame.Surface(((percent * self.width) / 100, self.height))

        pygame.draw.rect(self.bar, self.color, (0, 0, (percent * self.width) / 100, self.height), 0)
        self.bar_space.blit(self.bar, (0, 0))
        self.bar_space.blit(self.text, ((self.width / 2) - (self.text_size[0] / 2), (self.height / 2) - (self.text_size[1] / 2)))

        self.screen.blit(self.bar_space, (self.x, self.y))


    def set_color(self, color) -> None:
        """
        Set color of bar
        :param color: color of progress bar
        """
        self.color = color


    def set_alpha(self, alpha: float) -> None:
        """
        Set alpha of progress bar
        :param alpha: value of alpha
        """
        self.bar.set_alpha(alpha)
