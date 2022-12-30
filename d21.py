from typing import List
import time


def get_monkeys(data: List[str]):
    monkeys = {}
    for line in data:
        name, math = line.split(":")
        monkeys[name] = math.strip()
    return monkeys


def solve_part1(data: List[str]):
    """
    this is a kind of brute-foce solution.
    I'm not totally happy with it, but it works"""
    monkeys = get_monkeys(data)
    known: dict[str, int] = {}
    unknown: dict[str, str] = {}
    for name, math in monkeys.items():
        try:
            int(math)
        except ValueError:
            unknown[name] = math
        else:
            known[name] = int(math)
    # print(known)
    # print(unknown)
    while True:
        # loop over unknown monkey and check if their components are known
        # if that is the case, compute monkey, at to known and remove from unknown
        names_to_pop = []
        for name, math in unknown.items():
            first, operator, second = math.split()
            if first in known.keys() and second in known.keys():
                known[name] = eval(str(known[first]) + operator + str(known[second]))
                names_to_pop.append(name)
        for n in names_to_pop:
            unknown.pop(n)
        if "root" in known.keys():
            return known["root"]


def get_equation(name: str, monkeys: dict[str:str]):
    equation = name
    changed = True
    while changed:
        changed = False
        for mon in monkeys.keys():
            if mon in equation:
                equation = replace_names(equation, mon, monkeys)

                changed = True
    return equation


def replace_names(eq: str, name: str, monkeys: dict[str:str]):
    eq = eq.replace(name, "(" + monkeys[name] + ")")
    return eq


def solve_part2(data: List[str]):
    monkeys = get_monkeys(data)
    known: dict[str, int] = {}
    unknown: dict[str, str] = {}
    for name, math in monkeys.items():
        try:
            int(math)
        except ValueError:
            unknown[name] = math
        else:
            known[name] = int(math)
    # names to equalize
    left, _, right = unknown["root"].split()

    start_num = monkeys["humn"]
    left_eq = get_equation(left, monkeys)
    right_eq = get_equation(right, monkeys)
    # print(eval(left_eq), eval(right_eq))
    left_eq = left_eq.replace(str(start_num), "humn")
    right_eq = right_eq.replace(str(start_num), "humn")

    right_sol = eval(right_eq)

    best_humn = 10**12
    for mag in range(11, -1, -1):
        minimum = 10**15
        for i in range(
            best_humn - 2 * 10 ** (mag + 2), best_humn + 2 * 10 ** (mag + 2), 10**mag
        ):
            humn = i

            # print(f"ergebnis={eval(left_eq)}")
            calc = abs(eval(left_eq) - right_sol)
            if calc < minimum:
                minimum = calc
                best_humn = i
                # print(calc)
            elif calc > minimum:
                break
            if calc <= 0.1:
                return i


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = []
    for line in data:
        data_clear.append(line.strip())

    return data_clear


def main():

    data_clear = read_data("d21_input.txt")
    start = time.perf_counter()
    print("Solution Day 21, Part1:")
    print(solve_part1(data_clear))
    print(f"Runtime Part 1: {time.perf_counter() - start}")

    start = time.perf_counter()
    print("Solution Day 21, Part2:")
    print(solve_part2(data_clear))
    print(f"Runtime Part 2: {time.perf_counter() - start}")


if __name__ == "__main__":
    main()
