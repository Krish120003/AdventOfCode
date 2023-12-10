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
.....
.S-7.
.|.|.
.L-J.
.....
"""

TEST = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
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

# Find the single giant loop starting at S. How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

# The pipes are arranged in a two-dimensional grid of tiles:

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# ok lets first parse this into a grid
grid = []
for line in lines:
    grid.append(list(line))

ic(grid)

# ok now we need to find the starting point
start = None
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if col == "S":
            start = (x, y)
            break
ic(start)


# ok now we have to find a loop back to the start
# we can do this by following the path
# and then seeing if we ever hit a point we've already seen


g = {}  # graph of where we can go from each point

for x, row in enumerate(grid):
    for y, col in enumerate(row):
        g[(x, y)] = []

        if col == ".":
            continue

        elif col == "S":
            # well we are at S. lets check around it
            # and add the valid ones to the graph

            # check up
            if x > 0 and grid[x - 1][y] in "|7F":
                g[(x, y)].append((x - 1, y))

            # check down
            if x < len(grid) - 1 and grid[x + 1][y] in "|LJ":
                g[(x, y)].append((x + 1, y))

            # check left
            if y > 0 and grid[x][y - 1] in "-LF":
                g[(x, y)].append((x, y - 1))

            # check right
            if y < len(row) - 1 and grid[x][y + 1] in "-7J":
                g[(x, y)].append((x, y + 1))

        elif col == "|":
            # check up
            if x > 0 and grid[x - 1][y] in "S|7F":
                g[(x, y)].append((x - 1, y))

            # check down
            if x < len(grid) - 1 and grid[x + 1][y] in "S|LJ":
                g[(x, y)].append((x + 1, y))

        elif col == "-":
            # check left
            if y > 0 and grid[x][y - 1] in "S-LF":
                g[(x, y)].append((x, y - 1))

            # check right
            if y < len(row) - 1 and grid[x][y + 1] in "S-7J":
                g[(x, y)].append((x, y + 1))

        elif col == "L":
            # check up
            if x > 0 and grid[x - 1][y] in "S|7F":
                g[(x, y)].append((x - 1, y))

            # check right
            if y < len(row) - 1 and grid[x][y + 1] in "S-7J":
                g[(x, y)].append((x, y + 1))

        elif col == "J":
            # check up
            if x > 0 and grid[x - 1][y] in "S|7F":
                g[(x, y)].append((x - 1, y))

            # check left
            if y > 0 and grid[x][y - 1] in "S-LF":
                g[(x, y)].append((x, y - 1))

        elif col == "7":
            # check down
            if x < len(grid) - 1 and grid[x + 1][y] in "S|LJ":
                g[(x, y)].append((x + 1, y))

            # check left
            if y > 0 and grid[x][y - 1] in "S-LF":
                g[(x, y)].append((x, y - 1))

        elif col == "F":
            # check down
            if x < len(grid) - 1 and grid[x + 1][y] in "S|LJ":
                g[(x, y)].append((x + 1, y))

            # check right
            if y < len(row) - 1 and grid[x][y + 1] in "S-7J":
                g[(x, y)].append((x, y + 1))

        # ic(x, y, col, g[(x, y)])


# now we have a graph.
# find a loop in the graph starting from S
# we can do this efficiently by using a depth first search

# we can use a stack to do this

seen = set()
stack = [(start, 0, [start])]


loops = []

while stack:
    # pop the stack
    pos, steps, path = stack.pop()

    # have we seen this before?
    if pos in seen:
        if pos == start:
            print("We found start again!")
            loops.append((steps, path))
            continue
        else:
            continue

    # add it to seen
    seen.add(pos)

    # add its neighbors to the stack
    for neighbor in g[pos]:
        stack.append(
            (
                neighbor,
                steps + 1,
                path + [neighbor],
            )
        )

ic(loops)
actual_loop = max(loops, key=lambda x: x[0])

ic(actual_loop)

# ok now we have a loop
# find the point farthest from the start
# and the number of steps to get there

# we can do this by doing a breadth first search
distances = {
    start: 0,
}

queue = [start]

# while queue:
#     pos = queue.pop(0)

#     for neighbor in g[pos]:
#         if neighbor not in distances:
#             distances[neighbor] = distances[pos] + 1
#             queue.append(neighbor)

# ok now we have to find how many points are enclosed by the graph g

# lets do this with opencv lol
import numpy as np
import cv2

# # make a blank image
img = np.zeros((len(grid), len(grid[0]), 3), np.uint8)

# draw the loop
for pos in actual_loop[1]:
    img[pos[0], pos[1]] = (255, 255, 255)


# scale it up, but keep it like pixel art


import shapely

shape = shapely.Polygon(actual_loop[1])

c = 0
for x in tqdm(range(len(grid))):
    for y in range(len(grid[0])):
        if shape.contains(shapely.Point(x, y)):
            c += 1
            # make it green
            img[x][y] = (0, 255, 0)
        else:
            # if not in the shape, make it red
            if (x, y) not in actual_loop[1]:
                img[x][y] = (0, 0, 255)

# show img
img = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_NEAREST)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
