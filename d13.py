from typing import List
from itertools import zip_longest


def create_pairs(data: List[str]):
    list_of_pairs = []
    for i in range(0, len(data), 3):
        list_of_pairs.append([eval(data[i]), eval(data[i + 1])])
    return list_of_pairs


def create_pairs_part2(data: List[str]):
    list_of_pairs = []
    for dat in data:
        if dat != "":
            list_of_pairs.append(eval(dat))
    list_of_pairs.append(eval("[[2]]"))
    list_of_pairs.append(eval("[[6]]"))
    return list_of_pairs


def check_pair(pair: List):
    left = pair[0]
    right = pair[1]

    # print(f"compare {left} vs {right} ")
    for le, ri in zip_longest(left, right, fillvalue="empty"):
        # print(f"compare {le} vs {ri} ")

        if type(le) == int and type(ri) == int:
            # print("both are ints")
            if le < ri:
                # print("Left side is smaller, so inputs are in the right order")
                return True
            if ri < le:
                # print("right side is smaller, so inputs are not in the right order")
                return False
            if ri == le:
                continue
        if le == "empty":
            # print("Left side ran out of items, so inputs are in the right order")
            return True
        if ri == "empty":
            # print("Right side ran out of items, so inputs are not in the right order")
            return False

        if type(le) == list and type(ri) == list:
            check = check_pair([le, ri])
            if check == None:
                continue
            else:
                return check
        if type(le) == list and type(ri) == int:
            check = check_pair([le, [ri]])
            if check == None:
                continue
            else:
                return check
        if type(le) == int and type(ri) == list:
            check = check_pair([[le], ri])
            if check == None:
                continue
            else:
                return check


def solve_part1(data: List):
    right_indices = []
    for i, pair in enumerate(data, start=1):
        if check_pair(pair):
            right_indices.append(i)
    return sum(right_indices)


def bubble_sort_packets(packets: List):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(packets) - 1):
            if not check_pair([packets[i], packets[i + 1]]):
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
                swapped = True


def solve_part2(data: List):
    bubble_sort_packets(data)
    # for packet in data:
    #     print(packet)
    first = data.index([[2]]) + 1
    second = data.index([[6]]) + 1
    return first * second


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append(line.strip())

    return data_clear


def main():

    data_clear1 = read_data("d13_input.txt")
    pairs_part1 = create_pairs(data_clear1)

    print("Solution Day 13, Part1:")
    print(solve_part1(pairs_part1))

    data_clear2 = read_data("d13_input.txt")
    pairs_part2 = create_pairs_part2(data_clear2)
    # print(pairs_part2)
    print("Solution Day 13, Part2:")
    print(solve_part2(pairs_part2))


if __name__ == "__main__":
    main()
