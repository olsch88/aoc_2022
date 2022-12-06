from typing import List


def solve_part1(data: List[int]):

    return 0


def solve_part2(data: List[int]):

    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append((line[0], line[2]))

    return data_clear


def main():

    data_clear = read_data("dX_input.txt")

    print("Solution Day 1, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 1, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
