import pytest

from angrytux.model.game_objects.Obstacle import Obstacle
from angrytux.model.game_objects.Position import Position
import angrytux.model.game_objects.Obstacle
from angrytux.model.game_objects.obstacle_states.DestroyedState import DestroyedState
from angrytux.model.game_objects.obstacle_states.HittedState import HittedState
from angrytux.model.game_objects.obstacle_states.NewState import NewState


@pytest.fixture
def obstacle():
    return Obstacle(Position(50, 50))


def test_obstacle_hit_points(obstacle):
    init_hp = angrytux.model.game_objects.Obstacle.INITIAL_HIT_POINTS
    assert obstacle.hit_points == init_hp
    obstacle.got_hit()
    assert obstacle.hit_points == init_hp - 1
    obstacle.got_hit()
    assert obstacle.hit_points == init_hp - 2
    obstacle.got_hit()
    assert obstacle.hit_points == init_hp - 3


def test_obstacle_change_state_if_0_hit_points(obstacle, utils):
    for i in range(angrytux.model.game_objects.Obstacle.INITIAL_HIT_POINTS):
        obstacle.got_hit()

    assert utils.compare_classes(obstacle.state, DestroyedState(obstacle))


def test_obstacle_change_state_after_hit(obstacle, utils):
    assert utils.compare_classes(obstacle.state, NewState(obstacle))

    obstacle.got_hit()

    assert utils.compare_classes(obstacle.state, HittedState(obstacle))
