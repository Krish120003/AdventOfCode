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
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
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

from shapely import *

curr = (0, 0)
points_t = [curr]

exterior_points = 0

for line in lines:
    op, n, col = line.split(" ")

    n = int(n)

    col = col[2:-1]
    n = int(col[:5], 16)

    last = col[-1]

    # dig: 0 means R, 1 means D, 2 means L, and 3 means U.
    if last == "0":
        op = "R"
    if last == "1":
        op = "D"
    if last == "2":
        op = "L"
    if last == "3":
        op = "U"

    if op == "R":
        adj = (0, 1)

    if op == "L":
        adj = (0, -1)

    if op == "U":
        adj = (-1, 0)

    if op == "D":
        adj = (1, 0)

    curr = (curr[0] + adj[0] * n, curr[1] + adj[1] * n)
    points_t.append(curr)

    exterior_points += n


# visualize the points on grid

min_x = min([p[0] for p in points_t])
max_x = max([p[0] for p in points_t])
min_y = min([p[1] for p in points_t])
max_y = max([p[1] for p in points_t])

ic(min_x, max_x, min_y, max_y)

polygon = Polygon(points_t)

ic(polygon.area)
ic(exterior_points)
ic(polygon.area + exterior_points // 2 + 1)

exit()
grid = [["." for _ in range(max_y - min_y + 1)] for _ in range(max_x - min_x + 1)]

for p in points_t:
    grid[p[0] - min_x][p[1] - min_y] = "#"

for row in grid:
    print("".join(row))


# now lets fill inside the grid
from copy import deepcopy

new_grid = deepcopy(grid)


# lets flood fill


def flood_fill(grid, x, y, col):
    # iterative flood fill
    q = [(x, y)]

    while len(q) > 0:
        x, y = q.pop(0)

        if grid[x][y] == ".":
            grid[x][y] = col

            if x > 0:
                q.append((x - 1, y))
            if x < len(grid) - 1:
                q.append((x + 1, y))
            if y > 0:
                q.append((x, y - 1))
            if y < len(grid[0]) - 1:
                q.append((x, y + 1))


for i, row in enumerate(new_grid):
    for j, col in enumerate(row):
        if col == "#":
            # print in color
            print("\033[92m" + f"({i,j})" + "\033[0m", end=" ")

        else:
            print(f"({i,j})", end=" ")

    print()

fill_from = (311, 225)

print("=" * 10)
# ic(points_t)
flood_fill(new_grid, fill_from[0], fill_from[1], "#")

for row in new_grid:
    print("".join(row))

# count
count = 0

for row in new_grid:
    for col in row:
        if col == "#":
            count += 1

print(count)
