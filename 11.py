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
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
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

empty_rowss = set()
for x in range(len(grid)):
    if all(grid[x][y] == "." for y in range(len(grid[x]))):
        empty_rowss.add(x)

empty_colss = set()
for y in range(len(grid[0])):
    if all(grid[x][y] == "." for x in range(len(grid))):
        empty_colss.add(y)

non_empty_rowss = set(range(len(grid))) - empty_rowss
non_empty_colss = set(range(len(grid[0]))) - empty_colss

ic(empty_rowss, empty_colss)
points = []

pointers = {}

MUL = 1000000 - 1

# find all points
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == "#":
            # ok lets do some magic here.
            # we need to offset these points by the empty rows and cols

            # clearly, x and y are not empty rows and cols themselves
            # so we just need to find how many empty rows and cols are before x and y
            # but after the previous x and y

            dx = x
            dy = y

            empty_rows_on_top = len([x for x in empty_rowss if x < dx])
            empty_cols_on_left = len([y for y in empty_colss if y < dy])

            # now we can add these to the x and y
            dx += empty_rows_on_top * MUL
            dy += empty_cols_on_left * MUL

            points.append((dx, dy))


# loop over all pairs, but order doesnt matter
# for each pair, find their distance

pairs = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        pairs.append((points[i], points[j]))


distance = 0

for p1, p2 in pairs:
    x1, y1 = p1
    x2, y2 = p2

    e = abs(x1 - x2) + abs(y1 - y2)
    # ic(e)
    distance += e


ic(distance)
