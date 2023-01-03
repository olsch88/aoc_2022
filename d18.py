from dataclasses import dataclass, field
import numpy as np
from queue import SimpleQueue, Empty


@dataclass
class Cube:
    x: int
    y: int
    z: int
    neighbours: list = field(default_factory=list, repr=False)

    def is_neighbour(self, other: "Cube"):
        if (
            sum([abs(self.x - other.x), abs(self.y - other.y), abs(self.z - other.z)])
            == 1
        ):
            return True
        return False

    def get_free_sides(self):
        return 6 - len(self.neighbours)


def create_droplet_matrix(data: list[list[int]]):
    max_x = max([ele[0] for ele in data]) + 3
    max_y = max([ele[1] for ele in data]) + 3
    max_z = max([ele[2] for ele in data]) + 3
    matrix = np.zeros((max_x, max_y, max_z))
    for (
        entry
    ) in data:  # We add +1 to every coordinate, so no point is directly along an axis
        matrix[entry[0] + 1, entry[1] + 1, entry[2] + 1] = 1
    print(np.sum(matrix))
    return matrix


def traverse_matrix(matrix: np.ndarray) -> int:
    adjectend = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    queue = SimpleQueue()
    faces: int = 0
    visited = np.zeros(matrix.shape)
    visited[0, 0, 0] = 1
    queue.put([0, 0, 0])
    while True:
        try:
            next_elem = queue.get_nowait()
        except Empty:
            break
        for direc in adjectend:
            look = [
                next_elem[0] + direc[0],
                next_elem[1] + direc[1],
                next_elem[2] + direc[2],
            ]

            # ---- check for bounds
            if look[0] < 0 or look[1] < 0 or look[2] < 0:
                continue
            if (
                look[0] > matrix.shape[0] - 1
                or look[1] > matrix.shape[1] - 1
                or look[2] > matrix.shape[2] - 1
            ):
                continue
            # --- End of bounds check

            # look for a droplet face
            if matrix[look[0], look[1], look[2]] == 1:
                faces += 1
            # if it is empty, we put it on the queue
            elif (
                matrix[look[0], look[1], look[2]] == 0
                and visited[look[0], look[1], look[2]] == 0
            ):
                queue.put([look[0], look[1], look[2]])
                visited[look[0], look[1], look[2]] = 1
    return faces


def solve_part1(data: list[list[int]]):
    cubes: list[Cube] = []
    for line in data:
        cubes.append(Cube(line[0], line[1], line[2]))
    for cube1 in cubes:
        for cube2 in cubes:
            if cube1 == cube2:
                pass
            if cube2 not in cube1.neighbours and cube1.is_neighbour(cube2):
                cube1.neighbours.append(cube2)
    # print(cubes[1].neighbours)
    free_sides = 0
    for cube in cubes:
        free_sides += cube.get_free_sides()

    return free_sides


def solve_part2(data: list[list[int]]) -> int:
    max_x = max([ele[0] for ele in data])
    print(max_x)
    max_y = max([ele[1] for ele in data])
    print(max_y)
    max_z = max([ele[2] for ele in data])
    print(max_z)
    droplet_space = create_droplet_matrix(data)
    return traverse_matrix(droplet_space)


def read_data(input_file: str) -> list[list[int]]:
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append([int(x) for x in line.strip().split(",")])

    return data_clear


def main():

    data_clear = read_data("d18_input.txt")
    # print(data_clear)
    print("Solution Day 18, Part1:")
    # print(solve_part1(data_clear))
    print("Solution Day 18, Part2:")
    print(solve_part2(data_clear))
    # 1982 is to low


if __name__ == "__main__":
    main()
