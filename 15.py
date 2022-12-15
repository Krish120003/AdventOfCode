from math import *

# You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you imagine were originally built to locate lost Elves.

# The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors zoom off down the tunnels.

# Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. Each sensor knows its own position and can determine the position of a beacon precisely; however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. (There is never a tie where two beacons are the same distance to a sensor.)

# It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
# So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.

# Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

#                1    1    2    2
#      0    5    0    5    0    5
#  0 ....S.......................
#  1 ......................S.....
#  2 ...............S............
#  3 ................SB..........
#  4 ............................
#  5 ............................
#  6 ............................
#  7 ..........S.......S.........
#  8 ............................
#  9 ............................
# 10 ....B.......................
# 11 ..S.........................
# 12 ............................
# 13 ............................
# 14 ..............S.......S.....
# 15 B...........................
# 16 ...........SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....
# This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

#                1    1    2    2
#      0    5    0    5    0    5
# -2 ..........#.................
# -1 .........###................
#  0 ....S...#####...............
#  1 .......#######........S.....
#  2 ......#########S............
#  3 .....###########SB..........
#  4 ....#############...........
#  5 ...###############..........
#  6 ..#################.........
#  7 .#########S#######S#........
#  8 ..#################.........
#  9 ...###############..........
# 10 ....B############...........
# 11 ..S..###########............
# 12 ......#########.............
# 13 .......#######..............
# 14 ........#####.S.......S.....
# 15 B........###................
# 16 ..........#SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....
# This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

# None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

# So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, you'd like to count the number of positions a beacon cannot possibly exist. The coverage from all sensors near that row looks like this:

#                  1    1    2    2
#        0    5    0    5    0    5
#  9 ...#########################...
# 10 ..####B######################..
# 11 .###S#############.###########.
# In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

# Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?

TEST = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

PROD = """
Sensor at x=1326566, y=3575946: closest beacon is at x=1374835, y=2000000
Sensor at x=2681168, y=3951549: closest beacon is at x=3184941, y=3924923
Sensor at x=3959984, y=1095746: closest beacon is at x=3621412, y=2239432
Sensor at x=3150886, y=2479946: closest beacon is at x=3621412, y=2239432
Sensor at x=3983027, y=2972336: closest beacon is at x=4012908, y=3083616
Sensor at x=3371601, y=3853300: closest beacon is at x=3184941, y=3924923
Sensor at x=3174612, y=3992719: closest beacon is at x=3184941, y=3924923
Sensor at x=3316368, y=1503688: closest beacon is at x=3621412, y=2239432
Sensor at x=3818181, y=2331216: closest beacon is at x=3621412, y=2239432
Sensor at x=3960526, y=3229321: closest beacon is at x=4012908, y=3083616
Sensor at x=61030, y=3045273: closest beacon is at x=-467419, y=2369316
Sensor at x=3635583, y=3121524: closest beacon is at x=4012908, y=3083616
Sensor at x=2813357, y=5535: closest beacon is at x=3595763, y=-77322
Sensor at x=382745, y=1566522: closest beacon is at x=1374835, y=2000000
Sensor at x=3585664, y=538632: closest beacon is at x=3595763, y=-77322
Sensor at x=3979654, y=2158646: closest beacon is at x=3621412, y=2239432
Sensor at x=3996588, y=2833167: closest beacon is at x=4012908, y=3083616
Sensor at x=3249383, y=141800: closest beacon is at x=3595763, y=-77322
Sensor at x=3847114, y=225529: closest beacon is at x=3595763, y=-77322
Sensor at x=3668737, y=3720078: closest beacon is at x=3184941, y=3924923
Sensor at x=1761961, y=680560: closest beacon is at x=1374835, y=2000000
Sensor at x=2556636, y=2213691: closest beacon is at x=3621412, y=2239432
Sensor at x=65365, y=215977: closest beacon is at x=346716, y=-573228
Sensor at x=709928, y=2270200: closest beacon is at x=1374835, y=2000000
Sensor at x=3673956, y=2670437: closest beacon is at x=4029651, y=2547743
Sensor at x=3250958, y=3999227: closest beacon is at x=3184941, y=3924923
Sensor at x=3009537, y=3292368: closest beacon is at x=3184941, y=3924923
"""

x = TEST
x = PROD

data = x.strip().split("\n")
y = 10
y = 2000000


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


cannot = set()
beacons = set()

for line in data:
    first_half = line.split(":")[0]
    second_half = line.split(":")[1]
    x1, y1 = [int(x) for x in first_half.split("x=")[1].split(", y=")]
    x2, y2 = [int(x) for x in second_half.split("x=")[1].split(", y=")]

    # find distance between sensor and beacon
    d = dist(x1, y1, x2, y2)

    # find all points at y = 10 that are within d of sensor
    for i in range(x1 - d - 1_000_000, x1 + d + 1_000_000):
        if dist(i, y, x1, y1) <= d:
            cannot.add((i, y))

    # remove beacon from set
    beacons.add((x2, y2))

print(len(cannot - beacons))
