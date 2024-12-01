from collections import defaultdict
from collections import Counter
import math
import itertools
import collections

from tqdm import tqdm
from icecream import ic


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

PROD = """
"""

with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD

reflections = x.split("\n\n")

count = 0

for reflection in reflections:
    print("=" * 50)
    # we have to check where the reflection is

    # first check the rows
    rows = reflection.split("\n")
    columns = list(zip(*rows))
    row_found = False
    col_found = False

    for i in range(len(rows)):
        first_half = rows[: i + 1]
        second_half = rows[i + 1 :]

        if not first_half or not second_half:
            continue

        gen = list(zip(reversed(first_half), second_half))

        diff_chars = 0
        for x, y in gen:
            for a, b in zip(x, y):
                if a != b:
                    diff_chars += 1

        if diff_chars == 1:
            print("HORIZONTAL")
            ic(gen)

            ic(first_half, second_half, i + 1)

            count += (i + 1) * 100
            row_found = True
            break

    if row_found:
        continue

    for i in range(len(columns)):
        first_half = columns[: i + 1]
        second_half = columns[i + 1 :]

        if not first_half or not second_half:
            continue

        gen = list(zip(reversed(first_half), second_half))

        diff_chars = 0
        for x, y in gen:
            for a, b in zip(x, y):
                if a != b:
                    diff_chars += 1

        if diff_chars == 1:
            print("VERTICAL")
            ic(first_half, second_half, i + 1)
            col_found = True
            count += i + 1
            break

    if col_found:
        continue

    break

ic(count)
