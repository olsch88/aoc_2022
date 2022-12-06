import pytest
from ..d5 import solve_part1, solve_part2, read_body, read_header, reduce_body


@pytest.fixture
def sample_data():
    return read_data("d4_sample.txt")


def test_read_header():
    assert read_header("d5_sample.txt")[0] == "    [D]    \n"


def test_read_body():
    assert read_body("d5_sample.txt")[0] == "move 1 from 2 to 1"


def test_reduce_body():
    assert reduce_body(read_body("d5_sample.txt"))[0] == (1, 2, 1)
    assert reduce_body(read_body("d5_sample.txt"))[-1] == (1, 1, 2)


# def test_part1(sample_data):
#     assert solve_part1(sample_data) == 2


# def test_part2(sample_data):
#     assert solve_part2(sample_data) == 4
