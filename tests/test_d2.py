import pytest
from ..d2 import solve_part1, solve_part2, read_data


@pytest.fixture
def sample_data():
    return [("A", "Y"), ("B", "X"), ("C", "Z")]


def test_read(sample_data):
    read_data("d2_sample.txt") == sample_data


def test_part1(sample_data):
    assert solve_part1(sample_data) == 15


def test_part2(sample_data):
    assert solve_part2(sample_data) == 12
