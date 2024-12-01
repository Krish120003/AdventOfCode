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
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

PROD = """
"""


with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
x = PROD

import networkx as nx


lines = x.split("\n")


# we need undirected graph
G = nx.Graph()

for line in lines:
    a, b = line.split(": ")
    G.add_node(a)
    for c in b.split(" "):
        G.add_edge(a, c)


# visualize
import matplotlib.pyplot as plt

# plt.figure(3, figsize=(12, 12))

# nx.draw(G, with_labels=True)
# plt.show()

# nzn, pbq
# vfs, dhl
# xvp, zpc

# remove the above edges
G.remove_edge("nzn", "pbq")
G.remove_edge("vfs", "dhl")
G.remove_edge("xvp", "zpc")

# now find the sizes of the two components
for t in list(nx.connected_components(G)):
    print(len(t))
