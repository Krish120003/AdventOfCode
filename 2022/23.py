from copy import deepcopy
from math import *

# You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.

# "...but this volcano has been dormant for months. Without ash, the fruit can't grow!"

# You look up to see a massive, snow-capped mountain towering above you.

# "It's not like there are other active volcanoes here; we've looked everywhere."

# "But our scanners show active magma flows; clearly it's going somewhere."

# They finally notice you at the edge of the grove, your pack almost overflowing from the random star fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.

# "Why do you--" "How is--" "Did you just--"

# Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"

# The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.

# There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.

# For example:

# ....#..
# ..###.#
# #...#.#
# .#...##
# #.###..
# ##.#.##
# .#..#..
# The scan shows Elves # and empty ground .; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that north is up; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.

# The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of rounds during which Elves alternate between considering where to move and actually moving.

# During the first half of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf does not do anything during this round. Otherwise, the Elf looks in each of four directions in the following order and proposes moving one step in the first valid direction:

# If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
# After each Elf has had a chance to propose a move, the second half of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the only Elf to propose moving to that position. If two or more Elves propose moving to the same position, none of those Elves move.

# Finally, at the end of the round, the first direction the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.

# As a smaller example, consider just these five Elves:

# .....
# ..##.
# ..#..
# .....
# ..##.
# .....
# The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:

# ..##.
# .....
# ..#..
# ...#.
# ..#..
# .....
# Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south or west and proposes moving east. All five Elves succeed in moving to their proposed positions:

# .....
# ..##.
# .#...
# ....#
# .....
# ..#..
# Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:

# ..#..
# ....#
# #....
# ....#
# .....
# ..#..
# At this point, no Elves need to move, and so the process ends.

TEST = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

PROD = """
#...#.####.......###.#..##.#####.#...##.##.##.#.#.#...#.#...##...#..#.
#.#.####.#.#.###...#####.##..####..#.###...#.#...........#..#.#..##...
#.#####....#..###.#.###..##.#.#.#..#...###...####.#.##.#.#..#.###.#..#
.#..##.....##.##.#.#...##.#.##..#..##.#.#...#####...####..###...##..#.
##...###..##....##.#.#...#...#...##...#..#.#..##..###..##......####.#.
#..##.#.#...####.....###.#...#####.....##.##.#....#.#.......####..#.#.
..#.###....###..##.....#...#...#####....#.###.....###..###.#####..#...
#..###..##...##.#.#...##.#.#.#.###.#######.#.###...#..#.######....##.#
#.....###.....####.#..#...##..#.#.#...##....##.###.#.#...#.#.#..#.###.
.#...#......#......##..##.#....#.......##....##...#####...###..#.#.###
.#.####...#.###.##..##.#.#.##.##.####..####.###.#######..##...#..###..
.....##......#.#.##.######....#.#.#.#####.##.#.##...#.#..###.#.#.###..
.#.##.#.#.##..###.#..#...#####..##..#.#####...#....#..#.#...#.##.#....
.####...#....#.#.##.#.##.####......#......###....####.....#######....#
.###...########.##.#..#.#...#.##..####.##.#####.#..#.#....##...#...##.
#..###..####.#....#.#..#####.##.#.##...#.#.###.###.#.#....###...#.##.#
###..#.###.#.#####.###....###..#...##.###.#..##.####.#.#.#.###...##.#.
.#####.#..##..#...#.##.#..##.#.#.#...##.##..####..#.##.........#..##.#
.#.###...#....#.##.######..#...##.#...###.##...###...########..#.#.###
.######.#...##.####.##..#..#...#.#..##.##.#.##.#.#.#.##.#.###..##.##.#
#...####.#.#..##.#...##.#.#...##.#......####...#..#....##.##..#.###.#.
#....##..#.##....#######.#...#..#.####.##.....###.####.#.###..#..####.
..##..##.#....########..#.##.......#...#.#.........##.#.#..#....####..
.#..##.#.#.##...#.....##...##.#.#...#....#..#####.#..#..#.###..#.#.###
#.##.##............##.##.....##.#...#.#..##..#.#..###.....#..#..#..#.#
..#.....#..#..#.#.....#...###.#.#..#....##.##...#...##.##....#..##...#
..##...##.##......#...#..#####....#..#......###.#..#####...####.#....#
#..###.##..####.#....#..##.#..##.##.#.#..######.........#.##....######
..#.######.#.##...#..####..##....##..###.#.###.#.#..#.##.##.###.#..#.#
..#.####.###.#.#..###..#######.#..##.#....#.#####.###....#.#..###...##
....#....#..###.#...#......#..##...##..##.#.###...###.#.#.#.#..#...#.#
#....#..##..##.###.####.#######.###.###...#...#..###...#...#.#..#.##.#
#...###.##..#.#..#.#..#.#.#..###..####.##.##.#...###.#.###########...#
##...#...#...#..##....#...#...#....###.#######.....#.#.##...##..#.#..#
.....##.##.#.#.#..#..###....##.#....####.#.##.####..#.##.#..##.##.###.
....##.#....#####.#.##.........##.######.#..###..###..#.#.##.###.....#
...##..#####....##..####....##..###.##.##..##...#.#.###.#.#.##.#.##...
..#..####.#..#.##.##.#..####..#.#...##.....#...#....###..#.#.##..#.##.
#####.#..#.#.###..#.#.###.#######.#.#...#........##..#...#.##..#.##.#.
.#..###.###.#..##.####.##.###...#..#.#.....#.#.#...#....#.###..##.#.#.
.#.#.....##.##.#.####..##.#.#...#.#..#.....#..#....#......#.######.##.
...##.##..#....###...#..#.#..#.#.#.##..##.#..#.####..####.#.#.........
#.###.#...#....#...#.###.....#..#...##.#.#.####..#...#.#.#..####......
##.###.#.#####.#.##....#..#..##..##..#..##..##...#.#.##.##....#...##..
.###..###....#...##..###..#....###.....#..##...###.###.###..##.#..####
#.###........#..##.#.....#.....#...##.#####.#.##..##....####.#...##.#.
#.#.#..###.##.###..###..##..######..##.#####......#.##....##.#..###.#.
###...##.#.#.#.#.#.######...#..##.....#.#######.#..#..###.#.###.#...#.
###..######......#.###..#.....#########....#####.##..#...#.#...###..##
##.#..######..#.###..#.###.###.#.#####.####.....#...#.#...#####.#..##.
...####.#.#####.##...##..#.######.###....#.###.#.##.#####...#.#.#.####
#..###.########.#.###.#.####.###.###.#..#.##.#.#####..####.#.###...###
#..#.....#.###.#.##.###.#.....#..#....#####.#.#...##.###.######.###.##
##.#.#...###.#.#..#.#.###....###..#.##.#..#..###.#..#######.##.###.###
.##..##.#..#.#####.###.#.#.#......#.#.##.#...#.######.##...#.###.#####
#####....#.##....##.###..#.###..###.##...####.###.###..##.####.#.##.##
#......#.##.##.##.#....#.##.##..########.#....#..#..###.#####.#.#..##.
.#..#...#..##.#..###...#......##.##.###.....#.#.#.#..#.#####.##..#.###
.##.##.#.##.###..#..##.####.#.#..####.#.#.......##.......##.....#####.
####...##...#.#.#..###.#####.#.#.#.##.#..##......#.###.##..#...#...#.#
...........##.#.####.#.#########..###....#...#.......#..####..#####.#.
.#.###.##.#..####..#.###.#.#####..##.#......#.#..#####.##.#.###.#.##.#
###..#...#.##.####.#.##...#..#.......######...#....##....#.....#...#..
####.#.#...#.#.#######.##...#..#.#..#####...#..#.#..##.##.....##.##.#.
###..##..#..#.#.##.##..#..##..##..#####.#.##..##.####.##.##...#.####.#
#.##.#.#..##..####.....#.###..#....###.#.##.###.#.#.#.######.##....#..
.#.#..##..#.###.#.....##.##..##....####..#.#..#..##########.#...#...#.
###.####.#.#.##.#......#.###......##.###..##.##.#..#....#.##.#..#.....
.....##.......###.#..####.#.#.#.###..##...##...####.#.##.#.#.#..#.#.##
..##.##.#..#.##.....#...##.#...#.###..##.#.##...#..#.....###.#.#####..
"""

x = TEST
x = PROD

x = x.strip().split("\n")

# 8 directions
north_dirs = [(-1, 0), (-1, -1), (-1, 1)]
south_dirs = [(1, 0), (1, -1), (1, 1)]
west_dirs = [(0, -1), (-1, -1), (1, -1)]
east_dirs = [(0, 1), (-1, 1), (1, 1)]

dirs = list(set(north_dirs + south_dirs + west_dirs + east_dirs))

data = [[(0 if c == "." else 1) for c in line] for line in x]

n = 100
# add n extra rows and cols around the data
for i in range(n):
    data.insert(0, [0 for c in data[0]])
    data.append([0 for c in data[0]])
    for line in data:
        line.insert(0, 0)
        line.append(0)


# print(*data, sep="\n")
# print("-"*40)
for step in range(1000000):
    # FIRST HALF
    next_data = [[0 for c in line] for line in x]
    to_move_to = set()
    to_block = set()
    to_move = set()

    for i in range(len(data)):
        for j in range(len(data[0])):
            cell = data[i][j]
            if cell == 0:
                continue
            # print(i, j, cell)

            # this is an elf
            # check all 8 directions
            should_move = False
            for d in dirs:
                di, dj = d
                ni = i + di
                nj = j + dj
                if ni < 0 or ni >= len(data):
                    continue
                if nj < 0 or nj >= len(data[0]):
                    continue
                if data[ni][nj] != 0:
                    should_move = True
                    break

            if not should_move:
                # print("Elf at ({},{}) should not move".format(i, j))
                continue

            # FIRST HALF
            # find which direction to move to, by checking the 3 adjacent cells in that direction
            # check north, north east, north west
            start = (cell - 1 + step) % 4
            dirs_ordered = [north_dirs, south_dirs, west_dirs, east_dirs]
            # shift the dirs to the right by start
            dirs_ordered = dirs_ordered[start:] + dirs_ordered[:start]

            for d in dirs_ordered:
                # print(d)
                can_move_in_dir = True
                for di, dj in d:
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or ni >= len(data):
                        continue
                    if nj < 0 or nj >= len(data[0]):
                        continue
                    if data[ni][nj] != 0:
                        can_move_in_dir = False
                        # print("Elf at ({},{}) cannot move in direction {}".format(
                        # i, j, d), cell)

                if can_move_in_dir:
                    # if north, move to (i-1, j)
                    # if south, move to (i+1, j)
                    # if west, move to (i, j-1)
                    # if east, move to (i, j+1)
                    direction_name = ""
                    t = None
                    if d == north_dirs:
                        t = (i-1, j)
                        direction_name = "north"
                    elif d == south_dirs:
                        t = (i+1, j)
                        direction_name = "south"
                    elif d == west_dirs:
                        t = (i, j-1)
                        direction_name = "west"
                    elif d == east_dirs:
                        t = (i, j+1)
                        direction_name = "east"
                    # print("Elf at ({},{}) proposes moving in direction {}".format(
                        # i, j, direction_name))
                    if t in to_move_to:
                        to_block.add(t)
                    to_move_to.add(t)
                    to_move.add((i, j, t))
                    break
    if not to_move_to:
        # print("No one to move")
        print("BREAKING AT STEP", step)
        exit(0)
        break

    # # SECOND HALF
    next_data = deepcopy(data)
    for i, j, t in to_move:
        if t in to_block:
            # print("Elf at ({},{}) blocked".format(i, j))
            continue
        # print("Elf at ({},{}) moves to ({},{})".format(i, j, t[0], t[1]))
        next_data[i][j] = 0
        next_data[t[0]][t[1]] = 1

    data = next_data
    # print(*data, sep="\n")

    print("done step", step, end=" \r")

# find the leftmost and rightmost elves
leftmost = None
rightmost = None
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 1:
            if leftmost is None:
                leftmost = (i, j)
            rightmost = (i, j)

# find the top and bottom elves
topmost = None
bottommost = None
for j in range(len(data[0])):
    for i in range(len(data)):
        if data[i][j] == 1:
            if topmost is None:
                topmost = (i, j)
            bottommost = (i, j)

# find the min and max of the x and y coords
min_x = min(leftmost[0], rightmost[0])
max_x = max(leftmost[0], rightmost[0])
min_y = min(topmost[1], bottommost[1])
max_y = max(topmost[1], bottommost[1])

# count empty cells between the min and max x and y coords
count = 0
for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        if data[i][j] == 0:
            count += 1

print(count)
