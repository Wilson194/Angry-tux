import pygame

from controller.Commands.CannonDownCommand import CannonDownCommand
from controller.Commands.CannonStrenghtDownCommand import CannonStrengthDownCommand
from controller.Commands.CannonStrenghtUpCommand import CannonStrengthUpCommand
from controller.Commands.CannonUpCommand import CannonUpCommand
from controller.Commands.CannonAngleDownCommand import CannonAngleDownCommand
from controller.Commands.CannonAngleUpCommand import CannonAngleUpCommand
from controller.Commands.GravityDownCommand import GravityDownCommand
from controller.Commands.GravityUpCommand import GravityUpCommand
from controller.Commands.ShootCommand import ShootCommand
from controller.Commands.QuitCommand import QuitCommand
from controller.Commands.UndoCommand import UndoCommand
from .Commands.ChangeCannonStateCommand import ChangeCannonStateCommand
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
                    command = ChangeCannonStateCommand(self.__proxy)

                # Cannon power up - P
                if event.key == pygame.K_p:
                    command = CannonStrengthUpCommand(self.__proxy)

                # Cannon power down - o
                if event.key == pygame.K_o:
                    command = CannonStrengthDownCommand(self.__proxy)

                # Undo command
                if event.key == pygame.K_u:
                    command = UndoCommand()

                # Gravity up
                if event.key == pygame.K_g:
                    command = GravityUpCommand(self.__proxy)

                if event.key == pygame.K_f:
                    command = GravityDownCommand(self.__proxy)

            if command is not None:
                self._add_command(command)
        return 1


    def _add_command(self, command):
        self.__proxy.add_command(command)
