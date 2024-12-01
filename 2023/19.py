from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
import math
import itertools
import collections

from tqdm import tqdm
from icecream import ic

# increase recursion limit
import sys

# sys.setrecursionlimit(1000000)


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

PROD = """
"""


with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD

section = x.split("\n\n")

workflows = section[0].split("\n")
parts = section[1].split("\n")

# To start, each part is rated in each of four categories:

# x: Extremely cool looking
# m: Musical (it makes a noise when you hit it)
# a: Aerodynamic
# s: Shiny


@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int


def parse_part(s):
    # {x=787,m=2655,a=1222,s=2876}

    s = s.replace("{", "").replace("}", "")

    parts = s.split(",")
    parts = [p.split("=") for p in parts]
    parts = [(p[0], int(p[1])) for p in parts]

    return Part(*[p[1] for p in parts])


@dataclass
class Workflow:
    name: str
    rules: list


def parse_workflow(s):
    # px{a<2006:qkq,m>2090:A,rfg}

    name = s.split("{")[0]
    rules = s.split("{")[1][:-1]

    rules = rules.split(",")
    rules = [r.split(":") for r in rules]

    return Workflow(name, rules)


workflows = [parse_workflow(w) for w in workflows]
# parts = [parse_part(p) for p in parts]

workflows = {w.name: w for w in workflows}

workflows["R"] = Workflow("R", [])
workflows["A"] = Workflow("A", [])

# ic(workflows)

# accepted = []

# for part in parts:
#     current = workflows["in"]

#     while True:
#         if current.name in ["A", "R"]:
#             if current.name == "A":
#                 accepted.append(part)
#             break

#         for rule in current.rules:
#             if len(rule) == 2:
#                 cond = rule[0]

#                 # based on this condition, we need to find how many possible combinations of xmas there can be

#                 if cond:
#                     current = workflows[rule[1]]
#                     break

#             else:
#                 current = workflows[rule[0]]
#                 break

#     break


# ic(len(accepted))


# s = 0

# # add up all the x,m,a,s values
# for part in accepted:
#     s += part.x + part.m + part.a + part.s

# ic(s)


# Now we don't care about parts at all.

# All parts can have x,m,a,s from 1 to 4000
# we need to find ranges of values that are accepted by each workflow

# we can do this by going through each workflow and finding the ranges of values that are accepted

# we have to do this recursively

# we can start with the "in" workflow
start = "in"
start_ranges = {
    "x": [(1, 4000)],
    "m": [(1, 4000)],
    "a": [(1, 4000)],
    "s": [(1, 4000)],
}


from copy import deepcopy
import builtins


def get_ranges(name, ranges):
    current = workflows[name]

    if current.name in ["A", "R"]:
        if current.name == "A":
            return ranges

        else:
            return {
                "x": [],
                "m": [],
                "a": [],
                "s": [],
            }

    rule_ranges = []

    for rule in current.rules:
        # every rule will limit one of the values in some way

        if len(rule) == 1:
            # do this later

            continue

        else:
            new_ranges = deepcopy(ranges)
            # we have a condition
            cond = rule[0]
            next_workflow = rule[1]

            symbol = cond[0]
            sign = cond[1]
            value = int(cond[2:])

            if sign == "<":
                # we need to limit the upper bound of all the ranges
                new_ranges[symbol] = [(r[0], value - 1) for r in ranges[symbol]]

            elif sign == ">":
                # we need to limit the lower bound
                new_ranges[symbol] = [(value + 1, r[1]) for r in ranges[symbol]]

            # now we have to recurse
            new_ranges = get_ranges(next_workflow, new_ranges)
            rule_ranges.append(new_ranges)

            # now actually we have to adjust because the next rule is only reached if the current rule is false

    # now lets construct the final ranges

    actual_rangs = {}

    for range in rule_ranges:
        if not range:
            continue
        for key in range:
            if key not in actual_rangs:
                actual_rangs[key] = []

            actual_rangs[key].extend(range[key])

    return actual_rangs


t = get_ranges(start, start_ranges)
ic(t)

x = set()
m = set()
a = set()
s = set()

xv = 0
mv = 0
av = 0
sv = 0

for v in t["x"]:
    # check if range is valid, and if yes then add it to the set
    if v[0] < v[1]:
        xv += v[1] - v[0] + 1

    for value in builtins.range(v[0], v[1] + 1):
        x.add(value)


for v in t["m"]:
    if v[0] < v[1]:
        mv += v[1] - v[0] + 1
    for value in builtins.range(v[0], v[1] + 1):
        m.add(value)

for v in t["a"]:
    if v[0] < v[1]:
        av += v[1] - v[0] + 1

    for value in builtins.range(v[0], v[1] + 1):
        a.add(value)

for v in t["s"]:
    if v[0] < v[1]:
        sv += v[1] - v[0] + 1

    for value in builtins.range(v[0], v[1] + 1):
        s.add(value)


ic(len(x), len(m), len(a), len(s))

result = len(x) * len(m) * len(a) * len(s)
print(len(x) * len(m) * len(a) * len(s))

ic(167409079868000 - result * 2)

ic(xv, mv, av, sv)

ic(xv * mv * av * sv)
