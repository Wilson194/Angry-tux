import pygame

from controller.Commands.CannonDownCommand import CannonDownCommand
from controller.Commands.CannonUpCommand import CannonUpCommand
from controller.Commands.CannonAngleDownCommand import CannonAngleDownCommand
from controller.Commands.CannonAngleUpCommand import CannonAngleUpCommand
from controller.Commands.ShootCommand import ShootCommand
from controller.Commands.QuitCommand import QuitCommand
from model.Singleton import Singleton
from proxy.Proxy import Proxy


class Keyboard(metaclass=Singleton):
    """
    Keyboard controller
    """


    def __init__(self):
        self.__proxy = Proxy()


    def tick(self):
        """
        Parse all keyboard events
        :return:
        """
        for event in pygame.event.get():
            command = None
            if event.type == pygame.QUIT:
                command = QuitCommand()
            elif event.type == pygame.KEYDOWN:

                # Move cannon up - ^
                if event.key == pygame.K_UP:
                    command = CannonUpCommand(self.__proxy)

                # Move cannon down - v
                if event.key == pygame.K_DOWN:
                    command = CannonDownCommand(self.__proxy)

                # Angle cannon down - ->
                if event.key == pygame.K_RIGHT:
                    command = CannonAngleDownCommand(self.__proxy)

                # Angle cannon up - <-
                if event.key == pygame.K_LEFT:
                    command = CannonAngleUpCommand(self.__proxy)

                # Shoot - SPACE
                if event.key == pygame.K_SPACE:
                    command = ShootCommand(self.__proxy)

                # Change state - C
                if event.key == pygame.K_c:
                    command = ChangeStateCommand(self.__proxy)

            if command is not None:
                self._add_command(command)
        return 1


    def _add_command(self, command):
        self.__proxy.add_command(command)
