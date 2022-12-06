import pytest
from ..d6 import solve_part1, solve_part2, get_marker_position


# @pytest.fixture
# def sample_data():
#     return read_data("d4_sample.txt")


# def test_read_header():
#     assert read_header("d5_sample.txt")[0] == "    [D]    \n"


# def test_read_body():
#     assert read_body("d5_sample.txt")[0] == "move 1 from 2 to 1"


# def test_reduce_body():
#     assert reduce_body(read_body("d5_sample.txt"))[0] == (1, 2, 1)
#     assert reduce_body(read_body("d5_sample.txt"))[-1] == (1, 1, 2)
@pytest.mark.parametrize(
    "datastream,marker",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_marker_position4(datastream, marker):
    assert get_marker_position(datastream, 4) == marker


@pytest.mark.parametrize(
    "datastream,marker",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_marker_position14(datastream, marker):
    assert get_marker_position(datastream, 14) == marker
