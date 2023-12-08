from collections import defaultdict
from collections import Counter
import math
import itertools
import collections

# from icecream import ic


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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

pattern = lines[0]
lines = lines[2:]

# graph problem, but 2 edges each?

graph = {}

for line in lines:
    key = line.split(" = ")[0]
    value = line.split(" = ")[1]
    values = value[1:4], value[6:9]

    graph[key] = values


# traverse the graph based on the pattern
# until we get to the end
steps = 0

all_starting_nodes = [node for node in graph if node.endswith("A")]
# all_starting_nodes = ["AAA"]

current = all_starting_nodes

steps_min = []

# while True:
#     direction = 1 if pattern[steps % len(pattern)] == "R" else 0
#     steps += 1

#     if steps % 100000 == 0:
#         print(steps)

#     # compute all the new nodes
#     new_nodes = []
#     for node in current:
#         new_nodes.append(graph[node][direction])

#     # check if we are at the end
#     if all(node.endswith("Z") for node in new_nodes):
#         break

#     current = new_nodes

# print(steps)


# lets find how many steps it takes to get to end for each
# and find the lcm

# for each node, find the shortest path to the end
for node in all_starting_nodes:
    # print(node)
    current = node
    steps = 0

    while True:
        direction = 1 if pattern[steps % len(pattern)] == "R" else 0
        steps += 1

        # move to direction
        current = graph[current][direction]

        if current.endswith("Z"):
            break
        if steps < 100:
            print(current, steps)

    steps_min.append(steps)

print(steps_min)

# LCM is 12927600769609
# https://www.calculatorsoup.com/calculators/math/lcm.php
