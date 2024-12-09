import math
import collections
from collections import Counter
import re


TEST = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

PROD = """
..#....##....................#...#...#..........................................................................................#.
.....#..............................................#....#.....#.....#..............................#.......#...#.............#...
............#.#.........................................#...................#..#...........................###..........#.....#...
.....#.....#.............#...........................................................#.#.................#.........#..............
.......................#...........................#................#...........#......#.....................#...#.......#....#...
...#........................................#....................#.......#........##.##.........#.........................#.......
......#...........#....................#...........#.............................#........................#....................#..
...........................#...................................#...............#.........................................#........
........#...........#................................................................#............#...............................
.........................#......#.......#..............#......#.................#..................#...................#..........
............#......................................................#..............................#........#....#.................
........#.....................................................................#..............#....................................
..#............................#.................#.#............#.................................................................
...#................#.....................#.................................................#...................#.................
......#...................#........................................................................................#..#...........
.....................##..#........................................#...................#............#.....#........................
.......#.................#..........#...........................#.......#..............#..........................................
.............#........#........#..........#................#.........#.##.................................#.......#...........#...
.#..............................................................#..#.....................................#.................##.....
.........................#.#.......#.#..................................................#....................#.......#.........#..
.............#................................................#..#................#.............#.....#...........................
.............................................#..............#.....#..............#.........#......................................
................#............#............................#...........#.#.........................................................
...#.................................#.......#.........................................#..........................................
...............................#.....................................................................#.....#.........##...........
...................#...................................#.....................#.............................#..#...#...............
......#.......................................................#............................#......#.................#.#...........
...........................................#........................#.........#........................##......#..................
....#.......................#...................#.....#....................#......................................................
.....#......#....#..........#............#........#...............................................................................
.........#.................................................................................#........#.........................#...
........................#................................#........#...#......#........#..........#.#.......#.........#.........#.#
.##......#..#......#............#.#.................................#..............................#.........#....................
......#..............................#..........#.........#.....#....................................#...........................#
..#.........................#.#...#............................................#.#.......................................##.......
#.........................#......................#.............#..#.#...#....#.....#.#...#......#........................#........
.#............................#.................................#....#..............................#........#..........#.........
..........#.........#.....#.....#......................#............................................#.............................
.........................#...#.............................#..............................................#......#.#..............
....................#................................................................................................#............
...#........#......................#..#...........#..#.........#.................................................#................
...................#....................#..............#......................#..............#........#......................#....
.............#..................................................................................#................#.....##.........
.#.............................#........#................#..#..#.....#...........###..............................................
.......................................................#.........................#.............................#..................
...........................##.............#.........................................................#.......................#.....
......#.......##.........#..................................................................#.#..#.........#.........#.......#....
..#...........#..........#........#....#..........#..................#.............#.............#................................
#................................##...........#......#....##......#..#.....................................#.........#..#.........
...#...#.#.......................#......................................#.........#......#...............#........................
..#...#.......................................................#..................#.........................................#......
...#.....#.....#..........#....................#..................#.........................#...............#...#..#....#.........
..........#................................#...................#..#...........#.........#....................................#....
..............#........#............................#..................................................................#........#.
............................................................#.....##.................................#............................
...##..............................................#..........................................#.............................#.##..
...#...........................................................................#......#.....................#.#...................
.........#.............................................................................##.....................................#.#.
...............#.....#........#..#................................................................................................
#...........................#.#..............................#........^......#.................................#.....#............
...#...#.........................................#......................#.#.......................................................
.#......#...........................#.............................................................................................
.....#.........#.......#..#........#.....#.....................#......#........................................#...#..............
....#....................................................................................................#........................
#..............#.......................#.........................................#...............................#.#..............
................................#..............................#.......................................................#....#.....
....#............................#............................................................#.....#........#...................#
...........#...#............................#....................#.......................................................#........
.#.....................................................................................................#.....#....................
.#.......#..............#.....................#.....................#............#........................#.......................
............................#...#................................................#................................#...............
..........#...............#..........................#................#.........................#.......#.#.......................
..............................#.............................................................................................#.....
..............................................#....#...............................................#.....#........................
.........#...................................................#...............#.....#................#.............................
...........................................#..............#....................................................#........#.#.......
..........................#...........#.#...#.....................................#......................#...........#..#.........
....#...............#..............#.............................#....#.....#....#................................................
....#.#...........#..............#.................................................................#..............................
.....#.......#..........................................................................................#.#.......................
................................................#..#..............................................................................
.#....#..............................#..........#................#.............................................................#..
....#.......................#........#.....#..............#...............#..#........................................#...........
...........................................................................#......................................................
...#.........#..#.......................................................#..#..............................#.......................
.............#...................................................................#.......................#...#...........#........
.....#........................#....................#...................#................................#.........................
.........#......#...........................................#.......#....................#........................................
...........................................................#...........................#.............................#............
..........................#..............#........................................#......#.........#.#.............#........#.....
.........#..............#..#...........................#......#.......................#..#..#.............#.......................
...#.................#...............................................................................................#............
................#.....#.#...........................#......................#....................................#...#.#...........
..................#.....#...............................................................#............................#....#..#....
...............................#................................................#.............#..........................#........
..#...........#................................................#.........................................#...............##......#
...............................#..................##..#...........................................#................#..............
...........................#........#.........#....................................................#......#......#................
..................................#................#..................#.....#..................#...................#.....#........
.......#...#................................................................##...........................................#........
..............#..#.......#............................#...................#....#...........................#..#......#............
...............#............#................................................................................#..............#.....
...............#.....#........................#.........#.........#...#................#....#.........#...........................
................................#........................................................................#.........#..............
.............#..................#...#................................#..............#................................#.........#..
.....................#.#.............................#......#..................................#.........##....#.................#
......#.........#...#.................................#..........#.#......................#.......#........#......................
.....#....................#......................#.........#.....................#.........................................#......
.........##.....................#....#.#....#....................................................................................#
.................................................#.#....#....................#...............##..#................................
..##.......#........#.......................#.....................................................................#...........#.##
..#...........##........##......#..........#....................#.....#.....#..................#.....#............................
..........................#.......................#.....#.........................................................................
.#...........................#..............#...#...........#.....#.......#....#............#.....#..................#....#......#
.................#.......................#....#...#..................#......#............................#.....................#..
.....##..#........#........................#......#........................#....#......................##.........................
...#....................................................................................................#.......................#.
.......................#...#..............#..................#............#.#.........#....#...#..................................
...........#.......................#.......................#.......#....#.....#..................#...................#............
..................#......................................................................#.......#..........................#.....
.......#..................#.............#..#........##........#..##........##.....##...#................#..#.......#..............
........#................#..............................#..#......................................................................
...................#....#.........................#...........#.#......##.........#.#..................#..#.#....#........#.......
.............#......#.....................................................#.......................................................
.........................#.......................#..................#.........................#...............................#..#
..#...........................#............#.................##...#................#.................#................#...........
.....#...............#.....#..........#..................................#.#........................#.....###.#...................
...............................................#.............#......................................................#.............
......#......................#..............#.................#.#........#.................#......................................
........................#.......................................#....................#.......#.#..#...............................
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]

guard_pos = None

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            guard_pos = (i, j)
            grid[i][j] = "."
            break
    if guard_pos:
        break

print()

inital_pos = guard_pos
# from tqdm import tqdm

looped = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            # ok wehat if we block this?
            grid[i][j] = "#"
            guard_pos = inital_pos

            walked = set()
            cdir = (-1, 0)
            while True:
                x, y = guard_pos
                tmp = guard_pos + cdir
                if tmp in walked:
                    looped.add((i, j))
                    break
                walked.add(tmp)

                nx, ny = x + cdir[0], y + cdir[1]

                # if out of bounds
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    break

                # if wall
                if grid[nx][ny] == "#":
                    # turn right
                    cdir = (cdir[1], -cdir[0])
                    continue

                else:
                    # move forward
                    guard_pos = (nx, ny)
                    continue

            grid[i][j] = "."

# c = Counter(walked)

# print(len(walked))
print(len(looped))
