from typing import List


def get_marker_position(datastream: str, length) -> int:
    for i in range(length, len(datastream)):
        if len(set(datastream[i - length : i])) == length:
            return i


def solve_part1(data: str):

    return get_marker_position(data, 4)


def solve_part2(data: str):

    return get_marker_position(data, 14)


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readline()
    return data


def main():

    data_clear = read_data("d6_input.txt")

    print("Solution Day 6, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 6*, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
