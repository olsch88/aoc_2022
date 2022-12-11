import pytest
from ..d8 import solve_part1, solve_part2, read_data, get_scenic_score


@pytest.fixture
def sample_data():
    return [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


def test_read(sample_data):
    read_data("d8_sample.txt") == sample_data


def test_part1(sample_data):
    assert solve_part1(sample_data) == 21


def test_scenic(sample_data):
    assert get_scenic_score(sample_data, [1, 2]) == 4
    assert get_scenic_score(sample_data, [3, 2]) == 8


def test_part2(sample_data):
    assert solve_part2(sample_data) == 8
