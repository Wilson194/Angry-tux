from io import StringIO
import pytest
import sys
import copy
from angrytux.model.GameModel import GameModel
from angrytux.model.game_objects.Cannon import Cannon
from angrytux.model.game_objects.Position import Position
from angrytux.proxy.Proxy import Proxy
from pydoc import locate
import operator


def get_value(model, attributes):
    current = model
    for attribute in attributes.split('.'):
        current = getattr(current, attribute)

    return current


@pytest.mark.parametrize(['command', 'attributes', 'compare_operator'],
                         [('CannonAngleDownCommand', 'cannon.shooting_angle', 'lt'),
                          ('CannonAngleUpCommand', 'cannon.shooting_angle', 'gt'),
                          ('CannonStrengthDownCommand', 'cannon.strength', 'lt'),
                          ('CannonStrengthUpCommand', 'cannon.strength', 'gt'),
                          ('GravityDownCommand', 'gravity', 'lt'),
                          ('GravityUpCommand', 'gravity', 'gt'),
                          ])
def test_setters_commands_execute_and_undo_functions(command, attributes, compare_operator):
    model = GameModel()
    proxy = Proxy()
    result_std = StringIO()
    sys.stdout = result_std
    command = locate('angrytux.controller.Commands.{}.{}'.format(command, command))(proxy)

    old_value = get_value(model, attributes)

    command.execute()
    new_value = get_value(model, attributes)

    command.undo()
    undo_value = get_value(model, attributes)

    assert getattr(operator, compare_operator)(new_value, old_value)
    assert undo_value == old_value


@pytest.mark.parametrize(['command', 'compare_operator'], [('CannonDownCommand', 'gt'), ('CannonUpCommand', 'lt')])
def test_cannon_moving_commands_execute_and_undo_functions(command, compare_operator):
    model = GameModel()
    model._GameModel__cannon = Cannon(Position(0, 150))
    proxy = Proxy()
    result_std = StringIO()
    sys.stdout = result_std
    command = locate('angrytux.controller.Commands.{}.{}'.format(command, command))(proxy)

    old_position = copy.deepcopy(model.cannon.position)

    command.execute()
    new_position = copy.deepcopy(model.cannon.position)

    command.undo()
    undo_position = copy.deepcopy(model.cannon.position)

    assert getattr(operator, compare_operator)(new_position.y_position, old_position.y_position)
    assert int(new_position.x_position) == int(old_position.x_position)
    assert int(old_position.to_rect()[0]) == int(undo_position.to_rect()[0])
    assert int(old_position.to_rect()[1]) == int(undo_position.to_rect()[1])
