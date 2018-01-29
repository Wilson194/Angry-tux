import pygame
import pytest

from angrytux.config.Config import Config
from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
from angrytux.model.abstract_facotry.RealisticFactory import RealisticFactory
from angrytux.model.game_objects.Cannon import Cannon
from angrytux.model.game_objects.Position import Position

INIT_ANGLE = Config()['cannon_initial_shooting_angle']


def test_cannon_moving():
    cannon = Cannon(Position(50, 50))

    old_position = cannon.position.to_rect()
    cannon.move(90, 10)

    assert old_position != cannon.position.to_rect()


def test_cannon_change_state(utils):
    cannon = Cannon(Position(50, 50))

    old_state = cannon.state
    cannon.change_state()
    new_state = cannon.state

    assert not utils.compare_classes(old_state, new_state)


def test_cannon_single_shoot_create_one_missile(monkeypatch, callable_class):
    CreationFactory(RealisticFactory())
    monkeypatch.setattr(pygame, 'mixer', callable_class)
    cannon = Cannon(Position(50, 50))

    missiles = cannon.shoot()

    assert len(missiles) == 1
    missile = missiles[0]
    assert missile.movement_angle == cannon.shooting_angle
    assert missile.speed == cannon.strength


def test_cannon_double_shoot_create_two_missile(monkeypatch, callable_class):
    CreationFactory(RealisticFactory())
    monkeypatch.setattr(pygame, 'mixer', callable_class)
    cannon = Cannon(Position(50, 50))

    cannon.change_state()

    missiles = cannon.shoot()

    assert len(missiles) == 2
    missile1, missile2 = missiles
    assert missile1.speed == cannon.strength
    assert missile2.speed == cannon.strength
    assert missile1.movement_angle != missile2.movement_angle


def test_strength_setter_max_value():
    cannon = Cannon(Position(50, 50))

    assert cannon.strength == Config()['cannon_initial_strength']
    cannon.strength = Config()['cannon_max_strength'] + 20
    assert cannon.strength == Config()['cannon_max_strength']


def test_strength_setter_min_value():
    cannon = Cannon(Position(50, 50))

    assert cannon.strength == Config()['cannon_initial_strength']
    cannon.strength = 0
    assert cannon.strength == Config()['cannon_min_strength']


@pytest.mark.parametrize(['angle', 'result'],
                         [(10, INIT_ANGLE + 10),
                          (-10, INIT_ANGLE - 10),
                          (250, INIT_ANGLE),
                          (-250, INIT_ANGLE),
                          (0, INIT_ANGLE)])
def test_shooting_angle_function_max_and_min_values(angle, result):
    cannon = Cannon(Position(50, 50))

    cannon.angle(angle)
    assert cannon.shooting_angle == result
