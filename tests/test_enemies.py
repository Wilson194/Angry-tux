from angrytux.model.game_objects.Position import Position
import pytest
import importlib


@pytest.mark.parametrize('class_name', ('DumpEnemy', 'SmartEnemy', 'MovingEnemy'))
def test_enemy_return_come_collision_distance(class_name):
    module_ = importlib.import_module('angrytux.model.game_objects.enemies.{}'.format(class_name))
    class_ = getattr(module_, class_name)

    enemy = class_(Position(50, 50))

    assert enemy.collision_distance > 0


@pytest.mark.parametrize('class_name', ('DumpEnemy', 'SmartEnemy', 'MovingEnemy'))
def test_enemy_have_some_state(class_name):
    module_ = importlib.import_module('angrytux.model.game_objects.enemies.{}'.format(class_name))
    class_ = getattr(module_, class_name)

    enemy = class_(Position(50, 50))

    assert enemy.state is not None
