import math

from collections import * 
from itertools import combinations
from heapq import * 

from tqdm import tqdm
import re



PROD = """
wow
"""

TEST = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]

from functools import cache


total = 0
while True:
    accessible = 0
    to_clear = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                            if grid[ni][nj] == "@":
                                count += 1
                if count < 4:
                    accessible += 1
                    to_clear.append((i, j))
    for i, j in to_clear:
        grid[i][j] = "."
    if accessible == 0:
        break
    total += accessible

print(total)