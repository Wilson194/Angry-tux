from controller.Commands.Command import Command
from model.Commands import Commands
from model.ObjectsPackage import ObjectsPackage
from model.Observering.ChangeManager import ChangeManager
from model.Singleton import SingletonInheritance
from model.game_objects.Cannon import Cannon
from model.game_objects.Position import Position
from model.game_objects.enemies.DumpEnemy import DumpEnemy


class GameModel(SingletonInheritance):
    gravity = 9.81


    def __init__(self):
        self.__objects = ObjectsPackage()
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

        self.__objects.add_enemy(DumpEnemy(Position(400, 400)))

        self.__change_notify()


    def get_all_game_objects(self) -> list:
        """
        Return all game objects
        :return:
        """
        game_objects = self.__objects.get_all_objects()

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
        for missile in self.__objects.missiles:
            missile.move(self.gravity, self.__objects.get_all_collidable_objects())

        if self.__objects.missiles:
            return True
        else:
            return False


    def __act_enemies(self) -> bool:
        change = False
        for enemy in self.__objects.enemies:
            change = change or enemy.state.move()

        return change


    def __garbage_collector(self):
        """
        Destroy all object which is dead or out of window
        :return:
        """
        self.__objects.missiles = [missile for missile in self.__objects.missiles if not missile.state.delete]
        self.__objects.enemies = [enemy for enemy in self.__objects.enemies if not enemy.state.delete]


    def tick(self):
        """
        One moment in time, do all movements
        :return:
        """
        changed = self.__commands.do_commands()

        changed = self.__move_missiles() or changed

        changed = self.__act_enemies() or changed

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

        self.__objects.missiles.extend(missiles)


    def change_cannon_state(self):
        """
        Change cannon state
        """
        self.__cannon.change_state()


    def change_strength(self, strength: float):
        self.__cannon.strength += strength
