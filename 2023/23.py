# from collections import defaultdict
# from collections import Counter

# from dataclasses import dataclass
# import math
# import itertools
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
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
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

grid = {}

for x, line in enumerate(lines):
    for y, c in enumerate(line[1:-1]):
        grid[(x, y)] = c

max_x = max(x for x, y in grid.keys())
max_y = max(y for x, y in grid.keys())

start = (0, 0)
end = (max_x, max_y)


# find the longest path from start to end


class Graph:
    V: int
    graph: dict[int, set[int]]
    w: dict[int, int]
    last_big: int

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = {}

        self.w = {}

    # function to add an edge to graph
    def addEdge(self, u, v, w=1):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.w[u] = 1
            self.graph[u] = set([v])

        self.w[(u, v)] = w
        self.w[(v, u)] = w

    def compress(self):
        # find all the nodes that have only one neighbor
        # and remove them
        # and add the weight of the removed node to the neighbor
        # continue until no more nodes can be removed

        # remove nodes with only one neighbor
        while True:
            # find the first node with only two neighbors
            # and remove it
            f = None
            for node, edges in list(self.graph.items()):
                if (
                    len(edges) == 1
                    and node != pos_to_idx[start]
                    and node != pos_to_idx[end]
                ):
                    f = node

            # print("removing", f)

            if not f:
                break

            for neighbor in edges:
                # we just remove it
                self.graph[neighbor].remove(node)
            del self.graph[node]

        while True:
            # find the first node with only two neighbors
            # and combine it with its neighbors
            f = None
            for node, edges in list(self.graph.items()):
                if len(edges) == 2:
                    f = node

            # print("combining", f)

            if not f:
                break

            # combine it with its neighbors
            n1, n2 = self.graph[f]

            # print("removing", f, "and adding", n1, n2)
            # ic(self.graph)

            # remove the node
            del self.graph[f]
            self.graph[n1].remove(f)
            self.graph[n2].remove(f)

            # ic(self.graph)
            newW = self.w[(f, n1)] + self.w[(f, n2)]

            self.addEdge(n1, n2, newW)
            self.addEdge(n2, n1, newW)

            # ic(self.graph)

    # utility function to perform DFS and find all paths
    def _findAllPathsUtil(self, u, end, visited, path, allPaths):
        # if allPaths:
        #     weighted_paths = []

        #     for path in allPaths:
        #         weighted_paths.append(sum(g.w[node] for node in path))

        #     if max(weighted_paths) > self.last_big:
        #         self.last_big = max(weighted_paths)
        #         print("new big", self.last_big)
        # if allPaths:
        #     weighted_paths = []

        #     for path in allPaths:
        #         weighted_paths.append(
        #             sum(g.w.get((n1, n2), 0) for n1, n2 in zip(path, path[1:]))
        #         )

        #     w = max(weighted_paths) + 2

        #     if w > self.last_big:
        #         self.last_big = w
        #         print("new big", self.last_big)
        #     # self.last_big = max(self.last_big, )

        visited[u] = True
        path.append(u)

        if u == end:
            allPaths.append(list(path))
        else:
            if u in self.graph:
                for neighbor in self.graph[u]:
                    if not visited[neighbor]:
                        self._findAllPathsUtil(neighbor, end, visited, path, allPaths)

        path.pop()
        visited[u] = False

    # function to find all paths from start to end
    def findAllPaths(self, start, end):
        self.last_big = 0
        visited = {vertex: False for vertex in self.graph}
        allPaths = []
        path = []

        self._findAllPathsUtil(start, end, visited, path, allPaths)

        return allPaths

    def numEdges(self):
        return sum(len(edges) for edges in self.graph.values())


pos_to_idx: dict[tuple[int, int], int] = {pos: i for i, pos in enumerate(grid)}
# Driver's code
if __name__ == "__main__":
    g = Graph(len(grid))

    # add each edge but with -1 weight

    for (x, y), c in grid.items():
        if c == "#":
            continue

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in grid:
                if grid[(nx, ny)] == "#":
                    continue

                g.addEdge(pos_to_idx[(x, y)], pos_to_idx[(nx, ny)])

        continue

        if c == "v":
            # goes down
            nx, ny = x + 1, y
            if (nx, ny) in grid:
                if grid[(nx, ny)] == "#":
                    continue
                g.addEdge(pos_to_idx[(x, y)], pos_to_idx[(nx, ny)])

        elif c == ">":
            # goes right
            nx, ny = x, y + 1
            if (nx, ny) in grid:
                if grid[(nx, ny)] == "#":
                    continue
                g.addEdge(pos_to_idx[(x, y)], pos_to_idx[(nx, ny)])

        elif c == "<":
            # goes left
            nx, ny = x, y - 1
            if (nx, ny) in grid:
                if grid[(nx, ny)] == "#":
                    continue
                g.addEdge(pos_to_idx[(x, y)], pos_to_idx[(nx, ny)])

        elif c == "^":
            # goes up
            nx, ny = x - 1, y
            if (nx, ny) in grid:
                if grid[(nx, ny)] == "#":
                    continue
                g.addEdge(pos_to_idx[(x, y)], pos_to_idx[(nx, ny)])

    og = g.numEdges()
    g.compress()

    print("Compressed from", og, "to", g.numEdges())
    # ic(g.graph)
    # ic(g.w)

    # exit()
    l = g.findAllPaths(pos_to_idx[start], pos_to_idx[end])

    # for every path, find its weight
    weighted_paths = []

    for path in l:
        weighted_paths.append(sum(g.w[(n1, n2)] for n1, n2 in zip(path, path[1:])))

    ic(max(weighted_paths) + 2)  # its off by 2 for start and end
