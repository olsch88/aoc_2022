from typing import List
from dataclasses import dataclass, field
from itertools import count


@dataclass
class Point:
    x: int = 0
    y: int = 0


@dataclass
class Knot:
    ident: int = field(default_factory=count().__next__, init=False)
    pos: Point
    visited: List[Point] = field(default_factory=list, repr=False)


def sign(num: int):
    if num >= 0:
        return 1
    return -1


def follow(head: Knot, tail: Knot):
    if abs(head.pos.x - tail.pos.x) > 1 and abs(head.pos.y - tail.pos.y) == 1:
        tail.pos.x += (head.pos.x - tail.pos.x) - 1 * sign(head.pos.x - tail.pos.x)
        tail.pos.y += head.pos.y - tail.pos.y
    elif abs(head.pos.x - tail.pos.x) == 1 and abs(head.pos.y - tail.pos.y) > 1:
        tail.pos.x += head.pos.x - tail.pos.x
        tail.pos.y += (head.pos.y - tail.pos.y) - 1 * sign(head.pos.y - tail.pos.y)
    elif abs(head.pos.x - tail.pos.x) > 1 and abs(head.pos.y - tail.pos.y) > 1:
        tail.pos.x += (head.pos.x - tail.pos.x) - 1 * sign(head.pos.x - tail.pos.x)
        tail.pos.y += (head.pos.y - tail.pos.y) - 1 * sign(head.pos.y - tail.pos.y)
    elif abs(head.pos.x - tail.pos.x) > 1:
        tail.pos.x += (head.pos.x - tail.pos.x) - 1 * sign(head.pos.x - tail.pos.x)

    elif abs(head.pos.y - tail.pos.y) > 1:
        tail.pos.y += (head.pos.y - tail.pos.y) - 1 * sign(head.pos.y - tail.pos.y)

    tail.visited.append((tail.pos.x, tail.pos.y))
    # print(f"head: {head.pos}")
    # print(f"tail: {tail.pos}")


def process_step(knots: List[Knot], step: str):
    direction, amount = step.split()
    # print(direction, amount)
    for i in range(int(amount)):
        if direction == "R":
            knots[0].pos.x += 1
        elif direction == "L":
            knots[0].pos.x -= 1
        elif direction == "U":
            knots[0].pos.y += 1
        elif direction == "D":
            knots[0].pos.y -= 1
        for i in range(len(knots) - 1):
            follow(knots[i], knots[i + 1])


def solve_part1(data: List[str]):
    head = Knot(pos=Point())
    tail = Knot(pos=Point())
    knots = [head, tail]
    for step in data:
        process_step(knots, step)

    unique_points = []
    for point in tail.visited:
        if point not in unique_points:
            unique_points.append(point)
    return len(unique_points)


def solve_part2(data: List[str]):
    knots = [Knot(Point()) for _ in range(10)]
    for step in data:
        process_step(knots, step)
    # for knot in knots:
    #     print(knot)
    unique_points = []
    tail = knots[-1]
    for point in tail.visited:
        if point not in unique_points:
            unique_points.append(point)
    return len(unique_points)


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = [line.strip() for line in data]

    return data_clear


def main():

    data_clear = read_data("d9_input.txt")
    print(data_clear[0])

    print("Solution Day 9, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 9, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
