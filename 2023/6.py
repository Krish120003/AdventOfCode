from collections import defaultdict
from collections import Counter
import math
import itertools
import collections
from icecream import ic

from random import shuffle


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
Time:      7  15   30
Distance:  9  40  200
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


times = [int(e) for e in lines[0].split(":")[1].strip().split()]
distances = [int(e) for e in lines[1].split(":")[1].strip().split()]

mul = 1

t = "".join(str(e) for e in times)
t = int(t)

d = "".join(str(e) for e in distances)
d = int(d)

ways = 0
for i in range(t):
    speed = i
    time_to_travel = t - i
    distance = speed * time_to_travel
    if distance > d:
        ways += 1


print(ways)
