from typing import List, Tuple


def contains(ranges: Tuple[int]):
    min1, max1, min2, max2 = ranges
    if min1 >= min2 and max1 <= max2:
        return True
    if min2 >= min1 and max2 <= max1:
        return True
    return False


def overlap(ranges: Tuple[int]):
    min1, max1, min2, max2 = ranges
    if min2 > max1:
        return False
    if max2 < min1:
        return False
    return True


def solve_part1(data: List[Tuple[int]]):
    contain_count = 0
    for line in data:
        if contains(line):
            contain_count += 1
    return contain_count


def solve_part2(data: List[Tuple[int]]):
    overlap_count = 0
    for i, line in enumerate(data):
        if overlap(line):
            # print(i)
            overlap_count += 1
    return overlap_count


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        elf1, elf2 = line.strip().split(",")
        min1, max1 = elf1.split("-")
        min2, max2 = elf2.split("-")
        data_clear.append((int(min1), int(max1), int(min2), int(max2)))

    return data_clear


def main():

    data_clear = read_data("d4_input.txt")

    print("Solution Day 4, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 4, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
