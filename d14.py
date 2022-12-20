from typing import List
import numpy as np
from enum import Enum, auto
import matplotlib as mpl
from matplotlib import pyplot as plt


class Mat(Enum):
    AIR = 0
    SAND = 50
    ROCK = 100


def get_pair(text: str):
    pair = text.split(",")
    return [int(pair[0]), int(pair[1])]


def sign(x):
    if x < 0:
        return -1
    return 1


def create_cave(data: List[List], part2=False):
    """
    cave_values:
    0: air
    1: rock
    2: sand
    """
    cave = np.zeros((250, 1000), dtype=np.int8)
    y_max = 0
    for line in data:
        # print(line)
        for i in range(len(line) - 1):
            pair1 = get_pair(line[i])
            pair2 = get_pair(line[i + 1])
            for x in range(
                pair1[0],
                pair2[0] + 1 * sign(pair2[0] - pair1[0]),
                sign(pair2[0] - pair1[0]),
            ):

                for y in range(
                    pair1[1],
                    pair2[1] + 1 * sign(pair2[1] - pair1[1]),
                    sign(pair2[1] - pair1[1]),
                ):
                    if y > y_max:
                        y_max = y
                    cave[y, x] = Mat.ROCK.value

    if part2:
        cave[y_max + 2, :] = Mat.ROCK.value
    # print(cave)
    # print(cave[4, 502])

    # plt.imshow(cave, cmap="Greys", aspect="auto")
    # plt.show()
    return cave


def process_drop(cave: np.ndarray):
    current_drop = [0, 500]
    can_move = True
    max_depth = cave.shape[0] - 1
    while can_move:
        if current_drop[0] >= max_depth:
            break
        if cave[current_drop[0] + 1, current_drop[1]] == Mat.AIR.value:
            current_drop[0] += 1
        elif cave[current_drop[0] + 1, current_drop[1] - 1] == Mat.AIR.value:
            current_drop[0] += 1
            current_drop[1] -= 1
        elif cave[current_drop[0] + 1, current_drop[1] + 1] == Mat.AIR.value:
            current_drop[0] += 1
            current_drop[1] += 1
        else:
            can_move = False
            cave[current_drop[0], current_drop[1]] = Mat.SAND.value
            if current_drop == [0, 500]:
                return False

            return True

    return False


def solve_part1(cave: np.ndarray):
    sands = 0
    while True:

        if process_drop(cave):
            sands += 1
        else:
            break
    plt.imshow(cave, cmap="Greys", aspect="auto")
    plt.show()

    return sands


def solve_part2(cave: np.ndarray):
    sands = 0
    while True:
        if process_drop(cave):
            sands += 1
        else:
            sands += 1  # to account for the last grain of sand
            break

    plt.imshow(cave, cmap="Greys", aspect="auto")
    plt.show()

    return sands


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append(line.strip().split(" -> "))

    return data_clear


def main():

    cave_coord = read_data("d14_input.txt")
    cave_map = create_cave(cave_coord)
    # print("Solution Day 14, Part1:")
    # print(solve_part1(cave_map))
    cave_coord = read_data("d14_input.txt")
    cave_map = create_cave(cave_coord, part2=True)
    print("Solution Day 14, Part2:")
    print(solve_part2(cave_map))
    # 25584 to low


if __name__ == "__main__":
    main()
