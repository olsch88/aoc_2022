from typing import List


def read_header(input_file: str):
    with open(input_file, "r") as file:
        header = []
        for line in file.readlines():
            if line != "\n":
                header.append(line)
            else:
                break
    # print(header)
    return header[:-1]


def get_stacks_from_header(header: List[str]):
    no_of_stacks = int(len(header[0]) / 4)
    # print(no_of_stacks)

    stacks = [[] for x in range(no_of_stacks)]
    for line in header:
        print(line)
        for i in range(no_of_stacks):
            if line[1 + i * 4] != " ":
                stacks[i].append(line[1 + i * 4])
    # print(stacks)
    for stack in stacks:
        stack.reverse()
    return stacks


def read_body(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    body = []
    past_header = False
    for line in data:
        if line != "\n" and not past_header:
            continue
        if line == "\n":
            past_header = True
            continue
        body.append(line.strip())

    return body


def reduce_body(body: List[str]):
    """reduce the body to the numbers in the order"""

    reduced_body = []
    for line in body:
        parts = line.split()
        reduced = []
        for part in parts:
            try:
                reduced.append(int(part))
            except ValueError:
                continue
        reduced = tuple(reduced)
        reduced_body.append(reduced)

    return reduced_body


def process_step(stacks, step):
    amount, from_stack, to_stack = step
    for _ in range(amount):
        temp = stacks[from_stack - 1][-1:]
        stacks[from_stack - 1] = stacks[from_stack - 1][:-1]
        stacks[to_stack - 1] += temp
    # print(stacks)


def process_step_orderly(stacks, step):
    amount, from_stack, to_stack = step

    temp = stacks[from_stack - 1][-amount:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-amount]
    stacks[to_stack - 1] += temp


def solve_part1(stacks: List[str], steps: List[int]):
    for step in steps:
        process_step(stacks, step)

    return "".join([s[-1] for s in stacks])


def solve_part2(stacks: List[str], steps: List[int]):
    for step in steps:
        process_step_orderly(stacks, step)

    return "".join([s[-1] for s in stacks])


def main():

    data_clear = read_header("d5_input.txt")
    stacks = get_stacks_from_header(data_clear)

    steps = reduce_body(read_body("d5_input.txt"))

    print("Solution Day 5, Part1:")
    print(solve_part1(stacks, steps))

    data_clear = read_header("d5_input.txt")
    stacks = get_stacks_from_header(data_clear)

    steps = reduce_body(read_body("d5_input.txt"))
    print("Solution Day 5, Part2:")
    print(solve_part2(stacks, steps))

    # read_header("d5_sample.txt")


if __name__ == "__main__":
    main()
