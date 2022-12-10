from typing import List


def get_signal_at_cycle(insturctions: List[str], cycles: List[int]):
    """
    Return the Sum of cylce_no * signal (x) at each cycle_no in cycles
    """
    signal = 0
    cycle_counter = 0
    x = 1
    for command in insturctions:
        if command == "noop":
            cycle_counter += 1
            if cycle_counter in cycles:
                signal += cycle_counter * x
                # print(f"adding { cycle_counter * x} at cycle {cycle_counter}")
        else:  # if comand == "add ..."
            value = int(command.split()[1])
            for _ in range(2):
                cycle_counter += 1
                if cycle_counter in cycles:
                    signal += cycle_counter * x
                    # print(f"adding { cycle_counter * x} at cycle {cycle_counter}")
            x += value

    return signal


def solve_part1(data: List[str]):
    value = get_signal_at_cycle(data, [20, 60, 100, 140, 180, 220])
    return value


def solve_part2(data: List[int]):

    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append((line.strip()))

    return data_clear


def main():

    data_clear = read_data("d10_input.txt")

    print("Solution Day 10, Part1:")
    print(solve_part1(data_clear))

    print("Solution Day 10, Part2:")
    print(solve_part2(data_clear))


if __name__ == "__main__":
    main()