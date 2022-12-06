from typing import List


def solve_part1(data: List[int]):

    return 0


def solve_part2(data: List[int]):

    return 0


def read_header(input_file: str):
    with open(input_file, "r") as file:
        header = []
        for line in file.readlines():
            if line != "\n":
                print(len(line))
                header.append(line)
            else:
                break
    print(header)
    return header


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


def main():

    data_clear = read_header("d5_input.txt")

    # print("Solution Day 5, Part1:")
    # print(solve_part1(data_clear))
    # print("Solution Day 5, Part2:")
    # print(solve_part2(data_clear))

    read_header("d5_sample.txt")


if __name__ == "__main__":
    main()
