import pygame
from angrytux.controller.Commands.CannonAngleDownCommand import CannonAngleDownCommand
from angrytux.controller.Commands.CannonAngleUpCommand import CannonAngleUpCommand
from angrytux.controller.Commands.CannonDownCommand import CannonDownCommand
from angrytux.controller.Commands.CannonStrengthDownCommand import CannonStrengthDownCommand
from angrytux.controller.Commands.CannonStrengthUpCommand import CannonStrengthUpCommand
from angrytux.controller.Commands.CannonUpCommand import CannonUpCommand
from angrytux.controller.Commands.GravityUpCommand import GravityUpCommand
from angrytux.controller.Commands.QuitCommand import QuitCommand
from angrytux.controller.Commands.ShootCommand import ShootCommand
from angrytux.controller.Commands.UndoCommand import UndoCommand
from angrytux.controller.Commands.Command import Command
from angrytux.model.Singleton import Singleton
from angrytux.proxy.Proxy import Proxy

from angrytux.controller.Commands.GravityDownCommand import GravityDownCommand
from .Commands.ChangeCannonStateCommand import ChangeCannonStateCommand


class Keyboard(metaclass=Singleton):
    """
    Keyboard controller, this class control all actions from user
    Singleton class
    """


    def __init__(self) -> None:
        self.__proxy = Proxy()


    def tick(self) -> int:
        """
        Parse all keyboard events
        :return: 1 if everything is OK
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


    def _add_command(self, command: Command) -> None:
        """
        Add command to model queue
        :param command: created command
        """
        self.__proxy.add_command(command)
