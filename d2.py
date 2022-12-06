from typing import List

"""
A = Rock
B = Paper
C = Scissors

Part 1
X = Rock
Y = Paper
Z = Scissors

Part 2
X = loose
Y = draw
Z = win
"""

points_player = {"X": 1, "Y": 2, "Z": 3}
points_elf = {"A": 1, "B": 2, "C": 3}


def get_result(pair):
    # Draw
    if points_elf[pair[0]] == points_player[pair[1]]:
        return 3
    # rock beats scissors, paper beats rock
    if (
        (points_elf[pair[0]] == 1 and points_player[pair[1]] == 3)
        or (points_elf[pair[0]] == 2 and points_player[pair[1]] == 1)
        or (points_elf[pair[0]] == 3 and points_player[pair[1]] == 2)
    ):
        return 0
    return 6


def get_score(pair):
    points = points_player[pair[1]] + get_result(pair)
    return points


def solve_part1(data: List[int]):
    sum_of_points = 0
    for line in data:
        sum_of_points += get_score(line)
    return sum_of_points


def adapt_line(pair):
    if pair[0] == "A":
        if pair[1] == "X":
            return ("A", "Z")
        if pair[1] == "Y":
            return ("A", "X")
        if pair[1] == "Z":
            return ("A", "Y")
    if pair[0] == "B":
        if pair[1] == "X":
            return ("B", "X")
        if pair[1] == "Y":
            return ("B", "Y")
        if pair[1] == "Z":
            return ("B", "Z")
    if pair[0] == "C":
        if pair[1] == "X":
            return ("C", "Y")
        if pair[1] == "Y":
            return ("C", "Z")
        if pair[1] == "Z":
            return ("C", "X")


def solve_part2(data: List[int]):
    sum_of_points = 0
    for line in data:
        line = adapt_line(line)
        sum_of_points += get_score(line)
    return sum_of_points


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append((line[0], line[2]))

    return data_clear


def main():

    data_clear = read_data("d2_input.txt")

    print("Solution Day 1, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 1, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
