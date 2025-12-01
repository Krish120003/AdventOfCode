import math

from collections import * 
from itertools import * 
from heapq import * 
from tqdm import tqdm
import re

PROD = """
wow
"""

TEST = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
# grid = [list(line) for line in lines]

# dial goes up to 99, then goes back to 0
# 0 - 1 goes to 99

start = 50

# how many times zeor

result = 0

for line in lines:
    direction = line[0]
    amount = int(line[1:])

    for i in range(amount):
        if direction == "R":
            start += 1
            if start > 99:
                start = 0
        elif direction == "L":
            start -= 1
            if start < 0:
                start = 99

        if start == 0:
            result += 1

    print(start)

print(result)