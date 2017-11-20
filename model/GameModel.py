from controller.Commands.Command import Command
from model.Commands import Commands
from model.Observering.ChangeManager import ChangeManager
from model.Singleton import SingletonInheritance
from model.game_objects.Cannon import Cannon
from model.game_objects.Position import Position


class GameModel(SingletonInheritance):
    gravity = 9.81


    def __init__(self):
        self.__missiles = []
        self.__enemies = []
        self.__obstacles = []
        self.__commands = Commands()

        self.__cannon = Cannon(Position(0, 0))

        self.__score = 0
        self.running = False

        self.__changeManager = ChangeManager()

        self.__model_builder()


    def __model_builder(self):
        """
        Create initial object in model
        """
        self.__cannon = Cannon(Position(0, 150))

        self.__change_notify()


    def get_all_game_objects(self) -> list:
        """
        Return all game objects
        :return:
        """
        game_objects = []

        game_objects.extend(self.__missiles)
        game_objects.extend(self.__enemies)
        game_objects.extend(self.__obstacles)
        game_objects.append(self.__cannon)

        return game_objects


    def __change_notify(self):
        """
        Notify about model change (Observer)
        :return:
        """
        self.__changeManager.notify(self)


    def __move_missiles(self) -> bool:
        """
        Move all missiles
        :return: True if some missile move, False otherwise
        """
        for missile in self.__missiles:
            missile.move(self.gravity)

        if self.__missiles:
            return True
        else:
            return False


    def __garbage_collector(self):
        self.__missiles = [missile for missile in self.__missiles if not missile.state.delete]


    def tick(self):
        """
        One moment in time, do all movements
        :return:
        """
        changed = self.__commands.do_commands()

        changed = self.__move_missiles() or changed

        self.__garbage_collector()

        if changed:
            self.__change_notify()


    def add_command(self, command: Command):
        """
        Add command to Commands class
        :param command:
        :return:
        """
        self.__commands.add_command(command)


    def move_cannon(self, angle: float, distance: float):
        """
        Move cannon
        :param angle: angle of movement (90,-90)
        :param distance: distance of move
        """
        self.__cannon.position.move(angle, distance)
        self.__change_notify()


    def angle_cannon(self, angle: float):
        """
        Angle cannon
        :param angle: angle of move (+ up, - down)
        :return:
        """
        self.__cannon.angle(angle)


    def shoot(self):
        """
        Shoot missile from cannon
        """
        missiles = self.__cannon.shoot()

        self.__missiles.extend(missiles)


    def change_cannon_state(self):
        """
        Change cannon state
        """
        self.__cannon.change_state()


    def change_strength(self, strength: float):
        self.__cannon.strength += strength
