import math
import collections
from collections import Counter
import re
from tqdm import tqdm


TEST = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

PROD = """wow
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
# lines = x.split("\n")
# grid = [list(line) for line in lines]

result = 0

ranges, numbers = text.split("\n\n")

range_list = []
for line in ranges.split("\n"):
    a, b = line.split("-")
    range_list.append((int(a), int(b)))


range_list.sort()

merged = []

for a,b in range_list:
    if not merged:
        merged.append((a,b))
        continue

    if a > merged[-1][1]: # if the start of new is bigger than the end of the old
        merged.append((a,b))

    else: # extend the end to be larger of the two ends
        old = merged[-1]
        new = (old[0], max(old[1], b))
        merged[-1]= new


for a,b in merged:
    result += b - a + 1

print(result)