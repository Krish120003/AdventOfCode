from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
import math
import itertools
import collections
import heapq
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
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

TEST = """
111111111111
999999999991
999999999991
999999999991
999999999991
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

grid = [[int(c) for c in line] for line in lines]

from enum import Enum, auto


class Dir:
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


# 0,0 is top left

# Dijkstra's algorithm
# start will be the cost, position, direction, countdown, and path)


# x is the row
# y is the column

from functools import cache


# @cache
# def get_possible_neighbours(x, y, countdown, d):
#     n = set()
#     if x > 0:
#         n.add((x - 1, y))
#     if x < len(grid) - 1:
#         n.add((x + 1, y))
#     if y > 0:
#         n.add((x, y - 1))
#     if y < len(grid[0]) - 1:
#         n.add((x, y + 1))

#     # remove the one we cant go to
#     # but dont throw an error if we're at the edge

#     if d == Dir.UP:
#         n.discard((x + 1, y))

#     if d == Dir.DOWN:
#         n.discard((x - 1, y))

#     if d == Dir.LEFT:
#         n.discard((x, y + 1))

#     if d == Dir.RIGHT:
#         n.discard((x, y - 1))

#     # if countdown is 0, we can only go left or right based on the direction

#     if countdown == 1:
#         if d == Dir.UP or d == Dir.DOWN:
#             n.discard((x + 1, y))
#             n.discard((x - 1, y))
#         elif d == Dir.LEFT or d == Dir.RIGHT:
#             n.discard((x, y + 1))
#             n.discard((x, y - 1))

# return n


# start will be the cost, position, direction, countdown)


min_moves = 4
max_moves = 10

q = [(0, (0, 0), Dir.RIGHT), (0, (0, 0), Dir.DOWN)]

seen = set()

while q:
    cost, pos, dir = heapq.heappop(q)
    key = pos, dir

    if pos == (len(grid) - 1, len(grid[0]) - 1):
        ic(cost)
        break

    if key in seen:
        continue

    seen.add(key)

    possible_ddirs = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]

    if dir in [Dir.UP, Dir.DOWN]:
        possible_ddirs.remove(Dir.DOWN)
        possible_ddirs.remove(Dir.UP)

    else:
        possible_ddirs.remove(Dir.RIGHT)
        possible_ddirs.remove(Dir.LEFT)

    for d in possible_ddirs:
        i = 0
        c = 0
        while i < max_moves:
            i += 1
            # print(i)

            if d == Dir.UP:
                adjustment = (i, 0)

            if d == Dir.DOWN:
                adjustment = (-i, 0)

            if d == Dir.LEFT:
                adjustment = (0, -i)

            if d == Dir.RIGHT:
                adjustment = (0, i)

            new_pos = (pos[0] + adjustment[0], pos[1] + adjustment[1])

            if new_pos[0] < 0 or new_pos[0] >= len(grid):
                continue

            if new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
                continue

            c += grid[new_pos[0]][new_pos[1]]

            # we want the cost but we cant search this
            if i < min_moves:
                continue

            heapq.heappush(q, (cost + c, new_pos, d))
