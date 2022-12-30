from typing import List

snafu_map = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


def snafu_to_dec(snafu: str) -> int:
    length = len(snafu)
    snafu_int = 0
    for i in range(length):
        # print(snafu_map[snafu[i]] * 5 ** (length - i - 1))
        snafu_int += snafu_map[snafu[i]] * 5 ** (length - i - 1)
    return snafu_int


def dec_to_snafu(dec: int) -> str:
    snafu = ""
    while True:
        res = dec % 5
        div = dec // 5

        if res < 3:
            snafu = str(res) + snafu
        elif res == 3:
            snafu = "=" + snafu
            div += 1
        elif res == 4:
            snafu = "-" + snafu
            div += 1
        if div == 0:
            break
        dec = div

    return snafu


def solve_part1(data: List[str]):
    sum_dec = sum([snafu_to_dec(num) for num in data])
    return dec_to_snafu(sum_dec)


def solve_part2(data: List[int]):

    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data_clear = [line.strip() for line in data]

    return data_clear


def main():

    data_clear = read_data("d25_input.txt")

    # print(snafu_to_dec("3"))
    print(dec_to_snafu(3))
    print("Solution Day 25, Part1:")
    print(solve_part1(data_clear))
    # print("Solution Day 25, Part2:")
    # print(solve_part2(data_clear))


if __name__ == "__main__":
    main()
