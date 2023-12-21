from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
import math
import itertools
import collections

from tqdm import tqdm
from icecream import ic

# increase recursion limit
import sys

# sys.setrecursionlimit(1000000)


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

TEST2 = """
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##..S####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
.................................
.....###.#......###.#......###.#.
.###.##..#..###.##..#..###.##..#.
..#.#...#....#.#...#....#.#...#..
....#.#........#.#........#.#....
.##...####..##...####..##...####.
.##..#...#..##..#...#..##..#...#.
.......##.........##.........##..
.##.#.####..##.#.####..##.#.####.
.##..##.##..##..##.##..##..##.##.
.................................
"""

PROD = """
"""


with open("input.txt", "r") as f:
    PROD = f.read()

    # repeat every line 5 times
    # this is a hack to make the grid infinite
    # PROD = "\n".join([(line.replace("S", ".")) * 50 for line in PROD.split("\n")] * 50)

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD


cs = []

lines = x.split("\n")

grid = {}

for x, line in enumerate(lines):
    for y, c in enumerate(line):
        grid[(x, y)] = c
        if c == "S":
            start = (x, y)


start = (len(lines) // 2, len(lines[0]) // 2)
grid[start] = "."


for max_steps in range(65, 350, 131):
    done = {}
    q = [(start, 0)]

    # for

    while q:
        pos, steps = q.pop(0)

        # actually, the grid tiles infinitely in all directions
        # so we need to wrap around
        # pos = (pos[0] % len(lines), pos[1] % len(lines[0]))

        if pos in done:
            done[pos] += 1
            continue

        # if pos not in grid:
        #     continue

        to_check_pos = (pos[0] % len(lines), pos[1] % len(lines[0]))
        if grid[to_check_pos] == "#":
            continue

        if steps == max_steps:
            if pos not in done:
                done[pos] = 0
            done[pos] += 1
            continue

        if steps % 2 == (max_steps % 2):
            if pos not in done:
                done[pos] = 0
            done[pos] += 1

        x, y = pos

        q.append(((x + 1, y), steps + 1))
        q.append(((x - 1, y), steps + 1))
        q.append(((x, y + 1), steps + 1))
        q.append(((x, y - 1), steps + 1))

    print(max_steps, len(done))
# cs.append(len(done))


# print(cs)


# Hall of Failures
# 11839, 45847, 104773, 183457, 289314, 413042, 565700
# 2959,25621,72715,140107,234132

# Maybe?
# 3710,
# 32976,
# 91404,

# use wolfram to find polynomial
x = 202300
t = 3710 + (14685 * x) + (14581 * x * x)

# print every digit of t
s = ""
for i in range(1000):
    s += str(int(t) % 10)
    t /= 10
    if t < 1:
        break

print(s[::-1])


# 596734624269210
# FINALLY

# WOLFRAM ALPHA FOR THE WIN
