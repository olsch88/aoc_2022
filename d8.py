from typing import List
import numpy as np


def solve_part1(forrest: List[List[int]]):
    width = len(forrest[0])
    height = len(forrest)
    n_visible = 0

    for x in range(width):
        for y in range(height):
            if (
                x == 0 or y == 0 or x == width - 1 or y == height - 1
            ):  # Tree at the edge
                n_visible += 1
                continue

            size = forrest[y][x]
            ahead = forrest[y][x + 1 :]
            behind = forrest[y][:x]
            # above = forrest[:y][x] <- does not work like this
            above = [forrest[i][x] for i in range(y)]  # this does work as intendet
            # below = forrest[y + 1 :][x] <- does not work like this
            below = [
                forrest[i][x] for i in range(y + 1, height)
            ]  # this does work as intendet

            if (
                any([tree >= size for tree in ahead])
                and any([tree >= size for tree in behind])
                and any([tree >= size for tree in above])
                and any([tree >= size for tree in below])
            ):
                continue
            else:
                n_visible += 1
    return n_visible


def get_scenic_score(forrest: List[List[int]], position: List[int]) -> int:
    width = len(forrest[0])
    height = len(forrest)
    score_left = score_right = score_up = score_down = 0
    size = forrest[position[0]][position[1]]
    for x in range(position[1] - 1, -1, -1):
        # print(forrest[position[0]][x])
        if size > forrest[position[0]][x]:
            score_left += 1
        if size <= forrest[position[0]][x]:
            score_left += 1
            break
    # print(score_left)

    for x in range(position[1] + 1, width):
        if size > forrest[position[0]][x]:
            score_right += 1
        if size <= forrest[position[0]][x]:
            score_right += 1
            break
    # print(score_right)

    for y in range(position[0] - 1, -1, -1):
        if size > forrest[y][position[1]]:
            score_up += 1
        if size <= forrest[y][position[1]]:
            score_up += 1
            break
    # print(score_up)

    for y in range(position[0] + 1, height):
        if size > forrest[y][position[1]]:
            score_down += 1
        if size <= forrest[y][position[1]]:
            score_down += 1
            break
    # print(score_down)
    # print(score_left * score_down * score_right * score_up)
    return score_left * score_down * score_right * score_up


def solve_part2(forrest: List[List[int]]):
    width = len(forrest[0])
    height = len(forrest)
    score = []

    for x in range(width):
        for y in range(height):
            score.append(get_scenic_score(forrest, [y, x]))

    return max(score)


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    forrest = []
    for line in data:
        forrest.append([int(num) for num in line if num != "\n"])
    return forrest


def main():

    data_clear = read_data("d8_input.txt")

    print("Solution Day 1, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 1, Part2:")
    print(solve_part2(data_clear))

    # print("test1")
    # get_scenic_score(data_clear, [1, 2])
    # print("test2")
    # get_scenic_score(data_clear, [3, 2])


if __name__ == "__main__":
    main()
