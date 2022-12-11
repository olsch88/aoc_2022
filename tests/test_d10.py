import pytest
from ..d10 import solve_part1, solve_part2, read_data, get_signal_at_cycle


@pytest.fixture
def sample_data():
    return read_data("d10_sample.txt")


# def test_read(sample_data):
#     read_data("d8_sample.txt") == sample_data


def test_signal_simple1():
    assert get_signal_at_cycle(["noop", "addx 3", "addx -5"]) == [1, 1, 1, 4, 4]


def test_signal(sample_data):
    assert get_signal_at_cycle(sample_data)[20] * 20 == 420


def test_part1(sample_data):
    assert solve_part1(sample_data) == 13140


# def test_scenic(sample_data):
#     assert get_scenic_score(sample_data, [1, 2]) == 4
#     assert get_scenic_score(sample_data, [3, 2]) == 8


# def test_part2(sample_data):
#     assert solve_part2(sample_data) == 8
