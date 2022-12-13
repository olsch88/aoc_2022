import pytest
from ..d11 import solve_part1, solve_part2, read_data, monkey_factory


@pytest.fixture
def sample_data():
    return read_data("d11_sample.txt")


# def test_factory(sample_data):
#     assert monkey_factory(sample_data[0]) ==
