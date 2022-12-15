from typing import List
from dataclasses import dataclass, field


@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Head:
    pos: Point


@dataclass
class Tail:
    pos: Point
    visited: List[Point] = field(default_factory=list)


def process_step(head: Head, tail: Tail, step: str):
    direction, amount = step.split()
    print(direction, amount)
    pass


def solve_part1(data: List[str]):
    head = Head(pos=Point())
    tail = Tail(pos=Point())

    for step in data:
        process_step(head, tail, step)
    return 0


def solve_part2(data: List[str]):

    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = [line.strip() for line in data]

    return data_clear


def main():

    data_clear = read_data("d9_sample.txt")

    print("Solution Day 1, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 1, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
