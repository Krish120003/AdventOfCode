from collections import defaultdict
from collections import Counter
from dataclasses import dataclass
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
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

PROD = """
"""

with open("test.txt", "r") as f:
    TEST = f.read()

with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST

x = PROD

lines = x.split("\n")

# empty space (.), mirrors (/ and \), and splitters (| and -).

# 0,0 is top left
# beam enters from top left, going right

grid = [[c for c in line] for line in lines]


# uhh lets simulate a queue?


@dataclass
class BeamHead:
    x: int
    y: int

    # direction
    dx: int
    dy: int

    def __hash__(self):
        return hash((self.x, self.y, self.dx, self.dy))


max_energy = -1

possible_starts = []

# we can start from any of the edges
for i in range(len(grid)):
    # start from the left
    possible_starts.append(BeamHead(i, 0, 0, 1))
    # start from the right
    possible_starts.append(BeamHead(i, len(grid[0]) - 1, 0, -1))

for j in range(len(grid[0])):
    # start from the top
    possible_starts.append(BeamHead(0, j, 1, 0))
    # start from the bottom
    possible_starts.append(BeamHead(len(grid) - 1, j, -1, 0))


for start in tqdm(possible_starts):
    # start = BeamHead(0, -1, 0, 1)
    sims = [start]
    energized = set()
    already_simulated = set()

    hasnt_changed_in = 0
    last_energized = 0

    while sims:
        current = sims.pop(0)
        # print(len(sims))

        # ic("Looking at", current)

        if (current.x, current.y, current.dx, current.dy) in already_simulated:
            #     ic("Already simulated", current)
            continue

        already_simulated.add((current.x, current.y, current.dx, current.dy))

        # add to energized
        energized.add((current.x, current.y))

        # if len(energized) == last_energized:
        #     hasnt_changed_in += 1
        # else:
        #     hasnt_changed_in = 0
        #     last_energized = len(energized)

        # if hasnt_changed_in > 10000:
        #     break

        # move
        current.x += current.dx
        current.y += current.dy

        # check if we hit a wall
        if (
            current.x < 0
            or current.y < 0
            or current.x >= len(grid)
            or current.y >= len(grid[0])
        ):
            # print("Beam died", current)
            continue

        # check if we hit a splitter
        if grid[current.x][current.y] == "|":
            # print("hit a vertical splitter", current)
            if current.dy:
                # make 2 beams, one going up and one going down
                sims.append(BeamHead(current.x, current.y, 1, 0))
                sims.append(BeamHead(current.x, current.y, -1, 0))

            else:
                # keep going in the same direction
                sims.append(current)

        elif grid[current.x][current.y] == "-":
            # print("hit a horizontal splitter", current)
            if current.dx:
                # make 2 beams, one going left and one going right
                sims.append(BeamHead(current.x, current.y, 0, 1))
                sims.append(BeamHead(current.x, current.y, 0, -1))

            else:
                # keep going in the same direction
                sims.append(current)

        # check if we hit a mirror
        elif grid[current.x][current.y] == "\\":
            # print("hit a \ mirror", current)
            # if we're going up or down, we should go left or right
            if current.dy:
                sims.append(BeamHead(current.x, current.y, current.dy, 0))
            if current.dx:
                sims.append(BeamHead(current.x, current.y, 0, current.dx))

        elif grid[current.x][current.y] == "/":
            # print("hit a / mirror", current)
            # if we're going up or down, we should go left or right
            if current.dy:
                sims.append(BeamHead(current.x, current.y, -current.dy, 0))
            if current.dx:
                sims.append(BeamHead(current.x, current.y, 0, -current.dx))

        elif grid[current.x][current.y] == ".":
            # print("hit a .", current)
            # keep going in the same direction
            sims.append(current)

    # ic(sims)
    # print a grid of the energized points
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if (i, j) in energized:
    #             print("#", end="")
    #         else:
    #             print(".", end="")
    #     print()

    # input()

    max_energy = max(max_energy, len(energized))
print(max_energy)
# # print a grid of the energized points
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if (i, j) in energized:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
