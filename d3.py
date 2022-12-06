from typing import List
from itertools import cycle


def get_priority(char: str) -> int:
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 38


def get_double(line: str) -> str:
    half = int(len(line) / 2)
    part1 = set(line[:half])
    part2 = set(line[half:])
    double = part1 & part2
    return list(double)[0]  # should be only one


def solve_part1(data: List[str]):
    sum_of_priorities = 0
    for line in data:
        sum_of_priorities += get_priority(get_double(line))
    return sum_of_priorities


def solve_part2(data: List[str]):
    sum_of_group_priorities = 0
    iterate = cycle(range(3))
    cycler = list(next(iterate) for _ in range(len(data)))
    for i, line in zip(cycler, data):
        if i == 0:
            ruck0 = set(line)
        if i == 1:
            ruck1 = set(line)
        if i == 2:
            ruck2 = set(line)
            unique = ruck0 & ruck1 & ruck2
            sum_of_group_priorities += get_priority(list(unique)[0])

    return sum_of_group_priorities


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():

    data_clear = read_data(".\data\d3_input.txt")

    print("Solution Day 1, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 1, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
