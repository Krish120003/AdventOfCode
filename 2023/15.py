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
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

PROD = """
"""

with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD

groups = x.split(",")

s = 0


def hash(gc):
    t = 0
    for char in gc:
        # add ascii value of char
        t += ord(char)
        t *= 17
        t %= 256

    return t


m = defaultdict(list)
l = {}
for instruction in groups:
    op = "=" if "=" in instruction else "-"

    label = instruction.split(op)[0]
    labelHash = hash(label)

    value = instruction.split(op)[1]

    if op == "-":
        # remove label
        if label in m[labelHash]:
            m[labelHash].remove(label)

    elif op == "=":
        # add label
        if label not in m[labelHash]:
            m[labelHash].append(label)

        l[label] = value


s = 0
for box_n in range(256):
    box_power = 1 + box_n

    for j, v in enumerate(m[box_n]):
        s += box_power * int(l[v]) * (j + 1)


ic(s)
