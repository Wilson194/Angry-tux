import pygame
import pytest

from angrytux.model.game_objects.Missile import Missile
from angrytux.model.game_objects.Position import Position
from angrytux.model.game_objects.enemies.DumpEnemy import DumpEnemy
from angrytux.model.game_objects.enemies.enemy_states.HittedState import HittedState
from angrytux.model.game_objects.missile_states.Collided import Collided
from angrytux.model.game_objects.missile_states.OutOfGame import OutOfGame
from angrytux.model.game_objects.missile_strategies.SimpleMove import SimpleMove


@pytest.mark.parametrize(['angle', 'result'],
                         [(0, (60, 50)),
                          (90, (50, 40)),
                          (-90, (50, 60))])
def test_missile_basic_movement_without_collision(utils, angle, result):
    missile = Missile(Position(50, 50), 10, angle, SimpleMove())

    missile.move(10, [])

    assert utils.compare_rounded_tuple(missile.position.to_rect(), result)


def test_missile_collision_with_enemy(monkeypatch, callable_class):
    monkeypatch.setattr(pygame, 'mixer', callable_class)

    missile = Missile(Position(50, 50), 10, 0, SimpleMove())

    enemy = DumpEnemy(Position(50, 50))

    points = missile.move(10, [enemy])

    assert points == 10
    assert isinstance(enemy.state, HittedState)
    assert isinstance(missile.state, Collided)


def test_missile_change_state_out_of_window():
    missile = Missile(Position(50, 50), 100000, 0, SimpleMove())

    missile.move(10, [])

    assert isinstance(missile.state, OutOfGame)
