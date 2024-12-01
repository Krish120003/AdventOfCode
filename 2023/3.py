from collections import defaultdict
from collections import Counter
import math
import itertools
import collections
from icecream import ic

TEST = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
PROD = ""

with open("test.txt", "r") as f:
    PROD = f.read()

with open("input.txt", "r") as f:
    PROD = f.read()

TEST = TEST.strip()
PROD = PROD.strip()


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


to_ingore = ".0123456789"


def solve(x):
    lines = x.split("\n")

    data = [[c for c in line] for line in lines]
    dataT = list(zip(*data))

    # we look for symbols and find the numbers around them

    added = set()
    numbers = []

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell in to_ingore:
                continue

            this_cell_numbers = []
            added = set()

            # print("FOUND SYMBOL", cell, "at", i, j)
            if cell != "*":
                continue

            deltas = [1, 0, -1]

            for di in deltas:
                for dj in deltas:
                    if di == 0 and dj == 0:
                        continue

                    # compute the index to check
                    to_check = (i + di, j + dj)
                    x = to_check[0]
                    y = to_check[1]

                    if to_check in added:
                        continue

                    if data[x][y] in "0123456789":
                        # print("FOUND DIGIT", data[x][y], "at", x, y)

                        # since we have a single digit, we need to find the whole number
                        # we only need to check lefts/rights of this digit

                        start = y
                        end = y

                        # decrease start until we find a non-digit
                        while start >= 0 and data[x][start] in "0123456789":
                            start -= 1

                        # increase end until we find a non-digit
                        while end < len(data[x]) and data[x][end] in "0123456789":
                            end += 1

                        # we have the number
                        num = int("".join(data[x][start + 1 : end]))

                        # print("FOUND NUMBER", num, "at", x, start, end)

                        this_cell_numbers.append(num)

                        for k in range(start, end):
                            added.add((x, k))

            if len(this_cell_numbers) == 2:
                numbers.append(this_cell_numbers[0] * this_cell_numbers[1])

    # print(numbers)
    print(sum(numbers))


solve(TEST)
print("-----")
# try:
solve(PROD)
# except Exception as e:
#     print(e)
