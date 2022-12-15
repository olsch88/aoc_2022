from typing import List
from dataclasses import dataclass, field


@dataclass
class Node:
    name: str
    parent: "Node"
    children: List["Node"] = field(default_factory=list, repr=False)
    is_file: bool = False
    size: int = 0

    def get_size(self):
        self.size = 0
        for child in self.children:
            if child.is_file:
                self.size += child.size
                # print(f"adding{child.size}")
            else:
                self.size += child.get_size()
        return self.size


def get_node_by_name(node_list: List[Node], search_name):
    for node in node_list:
        if node.name == search_name:
            return node


def traverse_filesystem(output: List[str]):
    depth = 0  # 0 is at root level
    nodes = []
    current_node: Node
    root = Node("/", None, [], False)
    current_node = root
    nodes.append(root)
    for i, line in enumerate(output, start=2):
        if line == "$ ls":
            continue
        if line == "$ cd ..":
            # print(
            # f"trying to find parent of {current_node.name}, at depth: {depth};  Line {i}"
            # )
            # print(current_node.parent.name)
            current_node = current_node.parent
            depth -= 1
            continue
        if line.split()[1] == "cd":
            current_node = get_node_by_name(current_node.children, line.split()[2])
            # print(f"going to directory {current_node.name}, depth {depth}->{depth+1} ")
            depth += 1
            continue
        if "dir" in line:
            new_node = Node(name=line.split()[1], parent=current_node, children=[])
            current_node.children.append(new_node)
            nodes.append(new_node)
            # print(
            #     f"found directory {new_node.name} in  {current_node.name}, at depth: {depth}; Line {i}"
            # )
        else:
            try:
                size = int(line.split()[0])
                new_node = Node(
                    name=line.split()[1],
                    parent=current_node,
                    children=[],
                    is_file=True,
                    size=size,
                )
                current_node.children.append(new_node)
                nodes.append(new_node)
                # print(
                #     f"found file {new_node.name} in directory {current_node.name}, at depth: {depth}; Line {i}"
                # )
            except ValueError:
                pass
    return nodes


def solve_part1(data: List[str]):
    node_list = traverse_filesystem(data)
    sizes = [node.get_size() for node in node_list if not node.is_file]
    sizes_small = [size for size in sizes if size <= 100000]

    return sum(sizes_small)


def solve_part2(data: List[str]):
    total_space = 70000000
    space_needed = 30000000
    node_list = traverse_filesystem(data)
    sizes = [node.get_size() for node in node_list if not node.is_file]
    sizes.sort()
    total_size = max(sizes)
    unused = total_space - total_size
    for size in sizes:
        if unused + size >= space_needed:
            return size
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append(line.strip())

    return data_clear


def main():

    data_clear = read_data("d7_input.txt")[1:]
    # data_clear = read_data("d7_sample.txt")[1:]
    print("Solution Day 7, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 7, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
