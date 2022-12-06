import pytest
from ..d1 import solve_part1, solve_part2, read_data


@pytest.fixture
def sample_data():
    return [1000, 2000, 3000, 0, 4000, 0, 5000, 6000, 0, 7000, 8000, 9000, 0, 10000, 0]


def test_read(sample_data):
    read_data("d1_sample.txt") == sample_data


def test_part1(sample_data):
    assert solve_part1(sample_data) == 24000


def test_part2(sample_data):
    assert solve_part2(sample_data) == 45000
