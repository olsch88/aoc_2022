from collections import Counter


def move_item(li: list, item_index: int, amount: int) -> None:
    transfer = li.pop(item_index)
    li.insert((item_index + amount) % len(li), transfer)


def solve_part1(data: list[int]):
    start_data = data.copy()
    start_indexes = list(range(len(data)))
    new_indexes = list(range(len(data)))

    for i in range(len(data)):

        data_temp = data.copy()
        move_item(data, new_indexes.index(i), data[new_indexes.index(i)])
        move_item(new_indexes, new_indexes.index(i), data_temp[new_indexes.index(i)])

    index_0 = data.index(0)
    value_1000 = data[(index_0 + 1000) % len(data)]
    value_2000 = data[(index_0 + 2000) % len(data)]
    value_3000 = data[(index_0 + 3000) % len(data)]

    return value_1000 + value_2000 + value_3000


def solve_part2(data: list[int]):
    dec_key = 811589153
    for i, value in enumerate(data):
        data[i] = value * dec_key

    start_data = data.copy()
    start_indexes = list(range(len(data)))
    new_indexes = list(range(len(data)))

    for i in range(10):
        for i in range(len(data)):

            data_temp = data.copy()
            move_item(data, new_indexes.index(i), data[new_indexes.index(i)])
            move_item(
                new_indexes, new_indexes.index(i), data_temp[new_indexes.index(i)]
            )

    index_0 = data.index(0)
    value_1000 = data[(index_0 + 1000) % len(data)]
    value_2000 = data[(index_0 + 2000) % len(data)]
    value_3000 = data[(index_0 + 3000) % len(data)]

    return value_1000 + value_2000 + value_3000


def read_data(input_file: str) -> list[int]:
    with open(input_file, "r") as file:
        data = [int(line.strip()) for line in file.readlines()]
    return data


def main():

    data_clear = read_data("d20_input.txt")
    # print(data_clear)
    print("Solution Day 20, Part1:")
    print(solve_part1(data_clear))

    data_clear = read_data("d20_input.txt")
    print("Solution Day 20, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
