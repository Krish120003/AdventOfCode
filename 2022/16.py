from icecream import ic
from copy import copy, deepcopy
from tqdm import tqdm
from functools import lru_cache

# I learned a lot from
# https://nickymeuleman.netlify.app/garden/aoc2022-day16#part-2
# on how to approach part 2

# The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, and one of the elephants apparently figured out how to turn on the distress signal.

# The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

# You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, so you don't have time to go back out the way you came in.

# You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened (in pressure per minute) and the tunnels you could use to move between the valves.

# There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

# For example, suppose you had the following scan output:

# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II
# All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

# Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

# == Minute 1 ==
# No valves are open.
# You move to valve DD.

# == Minute 2 ==
# No valves are open.
# You open valve DD.

# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve CC.

# == Minute 4 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve BB.

# == Minute 5 ==
# Valve DD is open, releasing 20 pressure.
# You open valve BB.

# == Minute 6 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve AA.

# == Minute 7 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve II.

# == Minute 8 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve JJ.

# == Minute 9 ==
# Valves BB and DD are open, releasing 33 pressure.
# You open valve JJ.

# == Minute 10 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve II.

# == Minute 11 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve AA.

# == Minute 12 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve DD.

# == Minute 13 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve EE.

# == Minute 14 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve FF.

# == Minute 15 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve GG.

# == Minute 16 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve HH.

# == Minute 17 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You open valve HH.

# == Minute 18 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve GG.

# == Minute 19 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve FF.

# == Minute 20 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve EE.

# == Minute 21 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve EE.

# == Minute 22 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve DD.

# == Minute 23 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve CC.

# == Minute 24 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You open valve CC.

# == Minute 25 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 27 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 28 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 29 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 30 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
# This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

# Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

# from pprint import pprint as print
import sys

TEST = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

PROD = """
Valve DR has flow rate=22; tunnels lead to valves DC, YA
Valve IO has flow rate=14; tunnels lead to valves GE, CK, HY, XB
Valve XY has flow rate=0; tunnels lead to valves IP, AR
Valve UQ has flow rate=0; tunnels lead to valves XU, PD
Valve FO has flow rate=0; tunnels lead to valves DL, NC
Valve PU has flow rate=0; tunnels lead to valves ZJ, AN
Valve MK has flow rate=0; tunnels lead to valves ZS, SB
Valve HN has flow rate=0; tunnels lead to valves AA, DV
Valve XF has flow rate=0; tunnels lead to valves XB, AA
Valve OD has flow rate=13; tunnels lead to valves ZS, AF, SY, QQ, AR
Valve GE has flow rate=0; tunnels lead to valves KR, IO
Valve UF has flow rate=18; tunnels lead to valves QQ, AN, YE, GY
Valve WK has flow rate=19; tunnel leads to valve PQ
Valve PQ has flow rate=0; tunnels lead to valves WK, CW
Valve XU has flow rate=0; tunnels lead to valves DV, UQ
Valve SH has flow rate=0; tunnels lead to valves IP, AA
Valve SY has flow rate=0; tunnels lead to valves ZJ, OD
Valve OU has flow rate=0; tunnels lead to valves CK, DL
Valve IP has flow rate=8; tunnels lead to valves CY, ML, YI, XY, SH
Valve XZ has flow rate=0; tunnels lead to valves AM, PD
Valve ZU has flow rate=0; tunnels lead to valves CW, SB
Valve DC has flow rate=0; tunnels lead to valves CF, DR
Valve QY has flow rate=0; tunnels lead to valves CW, MQ
Valve XB has flow rate=0; tunnels lead to valves IO, XF
Valve AF has flow rate=0; tunnels lead to valves PD, OD
Valve GY has flow rate=0; tunnels lead to valves UF, ZC
Valve ZC has flow rate=0; tunnels lead to valves GY, CW
Valve ZJ has flow rate=25; tunnels lead to valves SY, PU
Valve NC has flow rate=6; tunnels lead to valves HY, ML, NJ, AT, FO
Valve DS has flow rate=0; tunnels lead to valves AT, DV
Valve DV has flow rate=7; tunnels lead to valves FD, KR, HN, DS, XU
Valve HY has flow rate=0; tunnels lead to valves NC, IO
Valve WF has flow rate=0; tunnels lead to valves NJ, AA
Valve CK has flow rate=0; tunnels lead to valves IO, OU
Valve YE has flow rate=0; tunnels lead to valves CY, UF
Valve LA has flow rate=0; tunnels lead to valves DL, ZM
Valve QQ has flow rate=0; tunnels lead to valves OD, UF
Valve AM has flow rate=0; tunnels lead to valves XZ, SB
Valve AN has flow rate=0; tunnels lead to valves UF, PU
Valve CL has flow rate=16; tunnels lead to valves YA, LD
Valve CF has flow rate=12; tunnel leads to valve DC
Valve FD has flow rate=0; tunnels lead to valves DV, DL
Valve QU has flow rate=0; tunnels lead to valves LD, PD
Valve AT has flow rate=0; tunnels lead to valves DS, NC
Valve SB has flow rate=24; tunnels lead to valves MK, AM, ZU
Valve YI has flow rate=0; tunnels lead to valves DL, IP
Valve ZM has flow rate=0; tunnels lead to valves AA, LA
Valve LD has flow rate=0; tunnels lead to valves CL, QU
Valve AR has flow rate=0; tunnels lead to valves OD, XY
Valve DL has flow rate=5; tunnels lead to valves FO, LA, YI, OU, FD
Valve MQ has flow rate=0; tunnels lead to valves QY, PD
Valve PD has flow rate=9; tunnels lead to valves MQ, QU, XZ, AF, UQ
Valve KR has flow rate=0; tunnels lead to valves GE, DV
Valve CY has flow rate=0; tunnels lead to valves YE, IP
Valve AA has flow rate=0; tunnels lead to valves SH, XF, ZM, HN, WF
Valve NJ has flow rate=0; tunnels lead to valves NC, WF
Valve YA has flow rate=0; tunnels lead to valves CL, DR
Valve ML has flow rate=0; tunnels lead to valves NC, IP
Valve CW has flow rate=15; tunnels lead to valves QY, PQ, ZC, ZU
Valve ZS has flow rate=0; tunnels lead to valves MK, OD
"""

x = TEST
x = PROD

x = x.strip().split("\n")

flows = {}
edges = {}


for line in x:
    name = line.split()[1]
    flows[name] = int(line.split("rate=")[1].split(";")[0])

    try:
        t = line.split("valves")[1].split(",")  # [1].split(", ")
    except IndexError:
        t = line.split("valve")[1].split(",")  # [1].split(", ")

    for v in t:
        if name not in edges:
            edges[name] = []
        edges[name].append(v.strip())

    temp = edges[name][:]


@lru_cache()
def distance_to_all(start):
    global edges
    G = edges
    dist = {}
    for v in G:
        dist[v] = sys.maxsize

    dist[start] = 0

    q = [start]

    while len(q) > 0:
        current = q.pop(0)
        for v in G[current]:
            # this line is very important
            # it makes sure we don't revisit a node
            # that we have already visited
            # by checking if the distance to the node
            # is already smaller than the current distance
            if dist[v] > dist[current] + 1:
                dist[v] = dist[current] + 1
                q.append(v)

    return dist


TIME = 26

all_values = set(edges.keys())

for k, v in flows.items():
    if v == 0:
        all_values.remove(k)

# simulate all possible paths
start_state = (
    "AA",  # current node
    0,  # time elapsed
    0,  # pressure released so far
    set(),  # open valves
)

q = [start_state]

best = 0
ops = 0
skipped = 0
already_checked = set()


@lru_cache()
def sorted_state(state: tuple):
    return tuple(sorted(state))


most_released_for_opening = {}

while q:
    ops += 1
    if ops % 10000 == 0:
        ic(len(q), best, ops, skipped)

    current, time, pressure, open = q.pop(0)

    most_released_for_opening[(tuple(open))] = max(
        most_released_for_opening.get((tuple(open)), 0),
        pressure,
    )

    if (time, pressure, tuple(open)) in already_checked:
        skipped += 1
        continue
    else:
        already_checked.add((time, pressure, tuple(open)))

    if time >= TIME:
        continue

    best = max(best, pressure)

    if len(open) == len(all_values):
        continue

    # we want to always go to one of the valves that is closed
    distance_to_all_from_current = distance_to_all(current)
    for valve in all_values - open:
        time_to_get_there = distance_to_all_from_current[valve]

        new_time = time + time_to_get_there + 1  # the +1 is the time to open it
        new_pressure = pressure + flows[valve] * (TIME - new_time)
        q.append(
            (
                valve,
                new_time,
                new_pressure,
                open.union({valve}),
            )
        )

    # ic(q)
    # input()

# print()
ic(ops)


best = 0
best_state = None

for k1 in tqdm(most_released_for_opening):
    for k2 in most_released_for_opening:
        ops += 1
        if ops % 10000 == 0:
            ic(ops, best, best_state)
        k1s = set(k1)
        k2s = set(k2)
        if len(k1s.intersection(k2s)) == 0:
            if most_released_for_opening[k1] + most_released_for_opening[k2] > best:
                best = most_released_for_opening[k1] + most_released_for_opening[k2]
                best_state = (k1, k2)

ic(best)
ic(best_state)


# The elephant opens
# DD, HH, EE
