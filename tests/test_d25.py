import pytest
from ..d25 import snafu_to_dec, dec_to_snafu


@pytest.fixture
def sample_data():
    with open("d25_sample.txt", "r") as file:
        sample_data = [line.strip() for line in file.readlines()]
    return sample_data


# def test_read(sample_data):
#     read_data("d8_sample.txt") == sample_data


@pytest.mark.parametrize(
    "snafu, decimal",
    [
        ("1=-0-2", 1747),
        ("12111", 906),
        ("2=0=", 198),
        ("21", 11),
        ("2=01", 201),
        ("111", 31),
        ("20012", 1257),
        ("112", 32),
        ("1=-1=", 353),
        ("1-12", 107),
        ("12", 7),
        ("1=", 3),
        ("122", 37),
    ],
)
def test_snafu_to_decimal(snafu, decimal):
    assert snafu_to_dec(snafu) == decimal


@pytest.mark.parametrize(
    "decimal, snafu",
    [
        (1, "1"),
        (2, "2"),
        (3, "1="),
        (4, "1-"),
        (5, "10"),
        (6, "11"),
        (7, "12"),
        (8, "2="),
        (9, "2-"),
        (10, "20"),
        (15, "1=0"),
        (20, "1-0"),
        (2022, "1=11-2"),
        (12345, "1-0---0"),
        (314159265, "1121-1110-1=0"),
    ],
)
def test_decimal_to_snafu(decimal, snafu):
    assert dec_to_snafu(decimal) == snafu


# def test_scenic(sample_data):
#     assert get_scenic_score(sample_data, [1, 2]) == 4
#     assert get_scenic_score(sample_data, [3, 2]) == 8


# def test_part2(sample_data):
#     assert solve_part2(sample_data) == 8
