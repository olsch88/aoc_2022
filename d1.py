from typing import List


def accululate_calories(data: List[int]) -> List[int]:
    cur_cal = 0
    list_of_calories = []
    for cal in data:
        if cal == 0:
            list_of_calories.append(cur_cal)

            cur_cal = 0
        else:
            cur_cal += cal

    list_of_calories.sort()

    list_of_calories.reverse()

    return list_of_calories


def solve_part1(data: List[int]):
    return max(accululate_calories(data))


def solve_part2(data):
    return sum(accululate_calories(data)[:3])


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        if line == "\n":
            data_clear.append(0)
        else:
            data_clear.append(int(line))
    data_clear.append(0)
    return data_clear


def main():

    data_clear = read_data("d1_input.txt")

    print("Solution Day 1, Part1:")
    print(solve_part1(data_clear))
    print("Solution Day 1, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
