from typing import List
from dataclasses import dataclass


def monkey_factory(data: List[str]):
    id = data[0].split()[1][0]
    items = data[1].split()[2:]
    items = [int(item.strip(",")) for item in items]
    operator = data[2].split("= ")[1]
    test = int(data[3].split()[-1])
    tru = int(data[4].split()[-1])
    fals = int(data[5].split()[-1])
    return Monkey(
        id_num=id,
        items=items,
        operation=operator,
        test=test,
        true_target=tru,
        false_target=fals,
    )


def prod(multis: List[int]):
    product = 1
    for num in multis:
        product = product * num
    return product


@dataclass
class Monkey:
    id_num: int
    items: List[int]
    operation: str
    test: int
    true_target: int
    false_target: int
    items_inspected: int = 0
    list_of_monkeys: List = None

    def inspect_item(self, item, part2=False):
        # start inspection by applying operation
        worry_level = self.apply_operation(item)
        # getting bored
        if not part2:
            worry_level = worry_level // 3
        if worry_level % self.test == 0:
            self.throw(worry_level, self.true_target, part2)
        else:
            self.throw(worry_level, self.false_target, part2)
        self.items_inspected += 1

    def apply_operation(self, old):
        # vaiable "old" is needed as part of the evaluated oparation"
        new = eval(self.operation)
        return new

    def throw(self, level, target, part2=False):
        self.items.pop(0)
        self.list_of_monkeys[target].recieve_item(level, part2)

    def recieve_item(self, item_wory_level, part2=False):
        divisor = [mon.test for mon in self.list_of_monkeys]
        divisor = prod(divisor)
        if part2:
            self.items.append(item_wory_level % divisor)
        else:
            self.items.append(item_wory_level)

    def turn(self, part2=False):
        for item in self.items.copy():  # need to copy, otherwise "pop(0)" wont work
            self.inspect_item(item, part2)

    def join_list(self, monkey_list: List):
        monkey_list.append(self)
        self.list_of_monkeys = monkey_list


def solve_part1(monkeys: List[Monkey]):
    for _ in range(20):
        for mon in monkeys:
            mon.turn()

    inspected = [mon.items_inspected for mon in monkeys]
    inspected.sort()

    return inspected[-1] * inspected[-2]


def solve_part2(monkeys: List[Monkey]):
    for _ in range(10000):
        for mon in monkeys:
            mon.turn(part2=True)
    # for mon in monkeys:
    #     print(mon.items_inspected)
    inspected = [mon.items_inspected for mon in monkeys]
    inspected.sort()

    return inspected[-1] * inspected[-2]


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]  # removing \n
    raw_monkeys = [data[i : i + 7] for i in range(0, len(data), 7)]
    # print(raw_monkeys)
    return raw_monkeys


def main():
    temp = []
    monkeys = []
    data_clear = read_data("d11_input.txt")
    for raw in data_clear:
        temp.append(monkey_factory(raw))
    for monkey in temp:
        monkey.join_list(monkeys)

    print("Solution Day 11, Part1:")
    print(solve_part1(monkeys))

    temp = []
    monkeys = []
    data_clear = read_data("d11_input.txt")
    for raw in data_clear:
        temp.append(monkey_factory(raw))
    for monkey in temp:
        monkey.join_list(monkeys)

    print("Solution Day 1, Part2:")
    print(solve_part2(monkeys))


if __name__ == "__main__":
    main()
