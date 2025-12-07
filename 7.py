import math
import collections
from collections import Counter
import re
from tqdm import tqdm


TEST = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

PROD = """
"""

x = TEST
x = PROD
x = x.strip("\n")

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
lines = [list(line) for line in lines]

result = 0

bs = set()

lines[1] = [(e if e != "S" else "|") for e in lines[0]]
lines.pop(0)



# BUILG GRAPH FROM P1
g = {}



s = 0
for i in range(0,len(lines)-1):
    curr = lines[i]
    nex = lines[i+1]

    for j, v in enumerate(curr):
        if v == "|" and nex[j] == "^":
            s += 1
            bs.add( (i+1,j-1) )
            lines[i+1][j-1] = "|"
            bs.add( (i+1,j+1) )
            lines[i+1][j+1] = "|"


            g[(i,j)] = [(i+1,j-1), (i+1,j+1)]
        elif v == "|":
            lines[i+1][j] = "|"
            g[(i,j)] = [(i+1,j)]
# print("\n".join("".join(line) for line in lines))
# print(bs)
# print(len(bs))
# print(s)

print(g)

from functools import cache

@cache
def dfs(u):
    neighbours = g.get(u, [])
    if len(neighbours) == 0:
        return 1
    
    res = 0
    for n in neighbours:
        res += dfs(n)
    return res

print(dfs((0, lines[0].index("|"))))


