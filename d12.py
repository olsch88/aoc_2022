from typing import List
import numpy as np
from dataclasses import dataclass, field

import sys

sys.setrecursionlimit(10**6)

heights = dict(zip("SabcdefghijklmnopqrstuvwxyzE", range(28)))


@dataclass
class Node:
    x: int = 0
    y: int = 0
    value: int = 0
    # neibours represents all adjcent fields that can be entered
    neighbours: List["Node"] = field(default_factory=list, repr=False)
    visited = False
    distance = 999999


def get_neighbours(maze: np.ndarray[Node], node: Node):
    """finding all possible destinations from a given node"""
    if not node.y - 1 < 0:
        neigh_val = maze[node.y - 1, node.x].value
        if neigh_val <= node.value + 1:
            node.neighbours.append(maze[node.y - 1, node.x])
    if not node.y + 1 >= maze.shape[0]:
        neigh_val = maze[node.y + 1, node.x].value
        if neigh_val <= node.value + 1:
            node.neighbours.append(maze[node.y + 1, node.x])

    if not node.x - 1 < 0:
        neigh_val = maze[node.y, node.x - 1].value
        if neigh_val <= node.value + 1:
            node.neighbours.append(maze[node.y, node.x - 1])
    if not node.x + 1 >= maze.shape[1]:
        neigh_val = maze[node.y, node.x + 1].value
        if neigh_val <= node.value + 1:
            node.neighbours.append(maze[node.y, node.x + 1])


# def traverse_node(cur_node: Node, cur_length=0, lengths=None):
#     """this is dfs, not bfs"""
#     cur_node.visited = True
#     length = cur_length
#     cur_node.distance = min(cur_length, cur_node.distance)
#     if cur_node.value == 27:  # End reached
#         lengths.append(cur_length)
#         # return cur_length

#     for neigh in cur_node.neighbours:  # [::-1]:
#         if not neigh.visited:
#             length = traverse_node(neigh, cur_length=cur_length + 1, lengths=lengths)
#     return  # length


# adaptiong an example found online:
def bfs(
    # maze: np.ndarray[Node],
    start_node: Node,
    target_node: Node,
):

    queue: List[Node] = []  # Initialize a queue
    distance = 0
    start_node.distance = distance
    start_node.visited = True
    queue.append(start_node)

    while queue:
        next_node = queue.pop(0)
        distance = next_node.distance
        # print(next_node)
        if next_node == target_node:
            return distance
        for neigh in next_node.neighbours:
            if not neigh.visited:
                neigh.distance = distance + 1
                neigh.visited = True
                queue.append(neigh)


def solve_part1(data: np.ndarray[Node]):
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            get_neighbours(data, data[i, j])
            if data[i, j].value == heights["S"]:
                start_node = data[i, j]
                start_node.value = heights["a"]

            if data[i, j].value == heights["E"]:
                end_node = data[i, j]
                end_node.value = heights["z"]

    return bfs(start_node, end_node)


def solve_part2(data: List[int]):

    return 0


def read_data(input_file: str):
    """
    takes the input text file and returns a numpy array of Nodes"""
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = [[] for _ in range(len(data))]
    for i, line in enumerate(data):
        for j, ch in enumerate(line.strip()):
            data_clear[i].append(Node(x=j, y=i, value=heights[ch]))
    data_np = np.array(data_clear)
    print(data_np)
    return data_np


def main():

    data_clear = read_data("d12_input.txt")

    print("Solution Day 12, Part1:")
    print(solve_part1(data_clear))
    # 2118 is to high

    print("Solution Day 12, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
