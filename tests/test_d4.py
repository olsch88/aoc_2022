import pytest
from ..d4 import solve_part1, solve_part2, read_data, overlap


@pytest.fixture
def sample_data():
    return read_data("d4_sample.txt")


@pytest.mark.parametrize(
    "ranges,result",
    [((2, 4, 6, 8), False), ((5, 7, 7, 9), True), ((5, 7, 1, 3), False)],
)
def test_overlap(ranges, result):
    assert overlap(ranges) == result


def test_read():
    assert read_data("d4_sample.txt")[0] == (2, 4, 6, 8)


def test_part1(sample_data):
    assert solve_part1(sample_data) == 2


def test_part2(sample_data):
    assert solve_part2(sample_data) == 4
