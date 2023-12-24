# from collections import defaultdict
# from collections import Counter

# from dataclasses import dataclass
# import math
import itertools

# import collections
# from typing import Tuple
# from tqdm import tqdm

from icecream import ic

# import random

# increase recursion limit
import sys


sys.setrecursionlimit(1000000)


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""


# TEST = """
# #.........#
# """

PROD = """
"""


with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD


lines = x.split("\n")

points = []

for line in lines:
    a, b = line.split("@")
    x, y, z = list(map(int, a.split(",")))

    vx, vy, vz = list(map(int, b.split(",")))

    points.append(((x, y, z), (vx, vy, vz)))

import numpy as np

# use numpy to find when point a and b are at the same position

from sympy import Point, Line


def find_intersection_point(point1, point2):
    x, y, _ = point1[0]
    vx_p, vy_p, _ = point1[1]

    a, b, _ = point2[0]
    vx_q, vy_q, _ = point2[1]

    coeff = 10000000000

    x2, y2 = x + vx_p * coeff, y + vy_p * coeff
    a2, b2 = a + vx_q * coeff, b + vy_q * coeff

    p1 = Point(x, y)
    p2 = Point(x2, y2)

    p3 = Point(a, b)
    p4 = Point(a2, b2)

    l1 = Line(p1, p2)
    l2 = Line(p3, p4)

    intersect = l1.intersection(l2)

    # make sure intersection was not in the past
    if intersect:
        temp = intersect[0]

        # the x should be same direction as vx_p
        if vx_p > 0 and temp[0] < x:
            return None
        elif vx_p < 0 and temp[0] > x:
            return None

        # the y should be same direction as vy_p
        if vy_p > 0 and temp[1] < y:
            return None
        elif vy_p < 0 and temp[1] > y:
            return None

        # the x should be same direction as vx_q
        if vx_q > 0 and temp[0] < a:
            return None
        elif vx_q < 0 and temp[0] > a:
            return None

        # the y should be same direction as vy_q
        if vy_q > 0 and temp[1] < b:
            return None
        elif vy_q < 0 and temp[1] > b:
            return None

    return intersect


result = 0


min_range = 7
max_range = 27

min_range = 200000000000000
max_range = 400000000000000

from tqdm import tqdm

# for a, b in tqdm(itertools.combinations(points, 2)):
#     if a == b:
#         continue

#     # ic(a, b)

#     ts = find_intersection_point(a, b)

#     if ts:
#         ts = ts[0]
#         if min_range <= ts[0] < max_range and min_range <= ts[1] < max_range:
#             result += 1
#             # ic(ts)

ic(result)

import z3


# we are solving for the points and velocitys of this magic rock we throw
# so they are unknown but reals (could be floats)
x_magic = z3.Real("x")
y_magic = z3.Real("y")
z_magic = z3.Real("z")
vx_magic = z3.Real("vx")
vy_magic = z3.Real("vy")
vz_magic = z3.Real("vz")

s = z3.Solver()

for i, point in enumerate(points):
    (x, y, z), (vx, vy, vz) = point

    # for every line we already have, we know that at a given time t
    # the x,y,z of this point will be the same as our magic
    t = z3.Real(f"t{point}")

    # use the same t for all 3 equations so they all happen at the same time
    s.add(
        x + vx * t == x_magic + vx_magic * t,
        y + vy * t == y_magic + vy_magic * t,
        z + vz * t == z_magic + vz_magic * t,
    )


s.check()
m = s.model()

print(m)

print(m[x_magic], m[y_magic], m[z_magic])
# add them
print(m[x_magic] + m[y_magic] + m[z_magic])

# 349084334634500 + 252498326441926 + 121393830576314
print(349084334634500 + 252498326441926 + 121393830576314)
