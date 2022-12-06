import pytest
from ..d3 import solve_part1, solve_part2, read_data, get_double, get_priority


@pytest.fixture
def sample_data():
    return read_data("d3_sample.txt")


def test_get_double():
    assert get_double("asfgghjk") == "g"


@pytest.mark.parametrize("chara,priority", [("a", 1), ("z", 26), ("A", 27), ("Z", 52)])
def test_priority(chara, priority):
    assert get_priority(chara) == priority


def test_read():
    assert read_data("d3_sample.txt")[0] == "vJrwpWtwJgWrhcsFMMfFFhFp"


def test_part1(sample_data):
    assert solve_part1(sample_data) == 157


def test_part2(sample_data):
    assert solve_part2(sample_data) == 70
