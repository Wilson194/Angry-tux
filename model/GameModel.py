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

        self.__cannon = None

        self.__score = 0
        self.running = False

        self.__changeManager = ChangeManager()

        self.model_builder()


    def model_builder(self):
        self.__cannon = Cannon(Position(0, 150))

        self.change_notify()


    def get_all_game_objects(self) -> list:
        game_objects = []

        game_objects.extend(self.__missiles)
        game_objects.extend(self.__enemies)
        game_objects.extend(self.__obstacles)
        game_objects.append(self.__cannon)

        return game_objects


    def change_notify(self):
        self.__changeManager.notify(self)


    def tick(self):
        changed = self.__commands.do_commands()

        if changed:
            self.change_notify()


    def add_command(self, command):
        self.__commands.add_command(command)


    def move_cannon(self, angle, distance):
        self.__cannon.position.move(angle, distance)
        self.change_notify()


    def angle_cannon(self, angle):
        self.__cannon.angle(angle)


    def shoot(self):
        pass
