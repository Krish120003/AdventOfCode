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
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

PROD = """
"""

with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD

lines = x.split("\n")

grid = [[c for c in line] for line in lines]


def make_list(grid):
    return [list(row) for row in grid]


def rotate_left(grid):
    return make_list(list(zip(*grid))[::-1])


def make_tuple(grid):
    return tuple(tuple(row) for row in grid)


T = make_list(zip(*grid))

from copy import deepcopy

OG_T = deepcopy(T)

s = 0


from functools import cache


@cache
def do_cycle(T):
    # if str(T) in memo:
    #     # print("FOUND LOOP")

    for _ in range(4):
        overall = []
        for col in T:
            col = "".join(col)
            sections = col.split("#")

            new_sections = ["".join(sorted(sec))[::-1] for sec in sections]

            updated = "#".join(new_sections)

            overall.append(updated)

        new_T = []
        for row in overall:
            new_T.append(list(row))

        T = new_T
        T = rotate_left(T)

    # memo.add(str(T))

    return make_tuple(T)


memo = {}

loop_start = None
loop_end = None

for i in tqdm(range(1000000000)):
    T = do_cycle(make_tuple(T))

    if T in memo:
        print("FOUND LOOP")
        ic(i)
        ic(memo[T])

        loop_start = memo[T]
        loop_end = i

        break
    memo[T] = i


# now we know the loop start and end
# so lets first simulate until the loop start

T = deepcopy(OG_T)
for i in tqdm(range(loop_start)):
    T = do_cycle(make_tuple(T))


leftover_cycles = 1000000000 - loop_start
# now we know that we loop back here. lets just do the remaining cycles
# and then we are done

cycle_size = loop_end - loop_start
to_skip_amount = (1000000000 - loop_end) // (cycle_size)

new_start = loop_start + to_skip_amount * cycle_size

ic(new_start)
ic(cycle_size, to_skip_amount)


for i in tqdm(range(new_start, 1000000000)):
    T = do_cycle(make_tuple(T))


# calculate load on north

for col in T:
    col = "".join(col)

    for i in range(len(col)):
        if col[i] == "O":
            s += len(col) - i

print(s)
