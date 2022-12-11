from typing import List


def get_signal_at_cycle(insturctions: List[str]):
    """
    Return the Sum of cylce_no * signal (x) at each cycle_no in cycles
    """

    signal = []

    cycle_counter = 0
    x = 1
    for command in insturctions:
        if command == "noop":
            cycle_counter += 1
            signal.append(x)
        else:  # if comand == "add ..."
            value = int(command.split()[1])
            for _ in range(2):
                cycle_counter += 1
                signal.append(x)
            x += value

    return signal


def solve_part1(data: List[str]):
    signals = get_signal_at_cycle(data)
    signal_strength_sum = 0
    sample_cycles = [20, 60, 100, 140, 180, 220]
    for cycle in sample_cycles:
        signal_strength_sum += cycle * signals[cycle - 1]
    return signal_strength_sum


def solve_part2(data: List[str]):
    cycle_positions = get_signal_at_cycle(data)  # index starts at 0
    crt = [["."] * 40 for _ in range(6)]
    for i in range(240):
        if i % 40 in range(cycle_positions[i] - 1, cycle_positions[i] + 2):
            crt[i // 40][i % 40] = "#"
    print(crt)
    return


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
