import math
import collections
from collections import Counter
import re
from pyparsing import col
from tqdm import tqdm


TEST = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

PROD = "wow"

x = TEST
x = PROD
# x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
# grid = [list(line) for line in lines]

result = 0

# things = [l.split() for l in lines]
things = lines
# things = list(zip(*things))



last_line = things[-1]
cols = []

for i in range(len(last_line)):
    if last_line[i] in ["+", "*"]:
        cols.append(i)    

print("Cols:", cols)



blobs = []

for i in range(len(cols)):
    c1 = cols[i]
    if i+1 >= len(cols):
        c2 = len(lines[0])
    else:
        c2 = cols[i+1]
    blob = []
    for line in things:
        blob.append(line[c1:c2])
    blobs.append(blob)

print(blobs)


for *stuff, op in blobs:

    stuff = ["".join(e) for e in list(zip(*[list(l) for l in stuff])) if "".join(e).strip() != ""]
    print(stuff)
    # exit()
    
    c = int(stuff[0].replace(" ", ""))
    for s in stuff[1:]:
        if "*" in op:
            c *= int(s.replace(" ", ""))
        elif "+" in op:
            c += int(s.replace(" ", "") )

    print(c)
    result += c
    # input()

print("Result:", result)



