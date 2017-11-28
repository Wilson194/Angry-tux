from angrytux.model.game_objects.Position import Position
import pytest


@pytest.mark.parametrize(['p1', 'p2', 'result'],
                         [((50, 50), (50, 100), 50),
                          ((50, 50), (100, 50), 50),
                          ((50, 50), (100, 100), 70),
                          ])
def test_compute_distance(p1, p2, result):
    position1 = Position(*p1)
    position2 = Position(*p2)

    assert int(position1.compute_distance_from(position2)) == result


@pytest.mark.parametrize(['angle', 'result'],
                         [(0, (60, 50)),
                          (90, (50, 40)),
                          (-90, (50, 60)),
                          (45, (57, 43))])
def test_move_function(utils, angle, result):
    p1 = Position(50, 50)

    p1.move(angle, 10)

    assert utils.compare_rounded_tuple(p1.to_rect(), result)


@pytest.mark.parametrize(['position', 'result'],
                         [((50, 50), False),
                          ((255, 485), False),
                          ((1555, 1555), True),
                          ((1500, 200), True)])
def test_position_out_of_window(position, result):
    position = Position(*position)

    assert position.out_of_window() == result
