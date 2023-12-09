from collections import defaultdict
from collections import Counter
import math
import itertools
import collections

from icecream import ic


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
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
s = 0
for line in lines:
    in_nums = list(reversed([int(x) for x in line.split()]))

    nums = [in_nums]

    while True:
        last = nums[-1]

        if all(0 == x for x in last):
            break

        new = []
        for i in range(len(last) - 1):
            new.append(last[i + 1] - last[i])

        nums.append(new)

    # now interpolate

    interp = 0
    for num_list in nums:
        interp += num_list[-1]

    ic(nums, interp)
    s += interp


print(s)
