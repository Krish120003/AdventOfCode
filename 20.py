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
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

TEST = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
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

# Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

low_pulses = 1000
high_pulses = 0

g = defaultdict(lambda x: [])
m = {}


# ft, jz, sv, ng all of these need to be high
class FlipFlop:
    def __init__(self, name):
        self.name = name
        self.state = 0

    def __repr__(self):
        return f"FlipFlop({self.name}, {self.state})"

    def pulse(self, sender, pulse, step=0):
        global low_pulses, high_pulses

        # if low pulse, then flip
        if pulse == 0:
            low_pulses += 1

            self.state = 1 - self.state
            return self.state
        else:
            # do nothing

            high_pulses += 1
            return None


class Conjunction:
    def __init__(self, name):
        self.name = name
        self.last_pulses = {}

    def __repr__(self):
        return f"Conjunction({self.name}, {self.last_pulses})"

    def pulse(self, sender, pulse, step=0):
        global low_pulses, high_pulses

        if pulse == 0:
            low_pulses += 1
        else:
            high_pulses += 1

        # update memory
        self.last_pulses[sender.name] = pulse

        # check if all pulses are high
        if all(self.last_pulses.values()):
            return 0
        else:
            # &nd -> hf
            # &pc -> hf
            # &vd -> hf
            # &tx -> hf
            if self.name in ["ft", "jz", "sv", "ng"]:
                # if self.name in ["nd", "pc", "vd", "tx"]:
                print(self.name, "is high", step)
            return 1

    @property
    def state(self):
        return 0 if all(self.last_pulses.values()) else 1


initial = []

conj_inputs = {}

for line in lines:
    left, right = line.split("->")
    left = left.strip()
    right = right.strip()

    if left.startswith("&"):
        conj_inputs[left[1:]] = []

for line in lines:
    left, right = line.split("->")
    left = left.strip()
    right = right.strip()

    if left.startswith("%"):
        m[left[1:]] = FlipFlop(left[1:])
        g[left[1:]] = [x.strip() for x in right.split(",")]

        for key in conj_inputs:
            if key in g[left[1:]]:
                conj_inputs[key].append(left[1:])

    elif left.startswith("&"):
        m[left[1:]] = Conjunction(left[1:])
        g[left[1:]] = [x.strip() for x in right.split(",")]

    elif left == "broadcaster":
        initial = [x.strip() for x in right.split(",")]

    else:
        raise Exception("unknown type")

# now set all conj last pulses to 0

for key in conj_inputs:
    for x in conj_inputs[key]:
        m[key].last_pulses[x] = 0


# ic(g)
# ic(m)
# ic(initial)
from tqdm import tqdm

for _ in tqdm(range(1, 500000)):
    q = initial[:]

    # send low pulse to all initial modules
    for x in initial:
        m[x].pulse(None, 0)

    while q:
        x = q.pop(0)

        # get module
        module = m[x]
        module_state_as_str = "high" if module.state else "low"

        # get connections
        connections = g[x]

        # get pulses
        pulses = []

        for y in connections:
            # print(x, f"-{module_state_as_str}>", y)
            # ic(module)
            modu = m.get(y, None)
            if not modu:
                # well, we still sent a pulse to it
                if module.state == 0:
                    low_pulses += 1
                else:
                    high_pulses += 1

                continue

            pulse = modu.pulse(module, module.state, _)

            pulses.append(pulse)

        # add new pulses to queue
        for i, p in enumerate(pulses):
            if p is not None:
                q.append(connections[i])

    # ic(x, module, connections, pulses, q)

    # now that we are done simulating a button press, check if any of ft, jz, sv, ng are high

# ic(m)
# ic(g)
ic(low_pulses, high_pulses)

ic(low_pulses * high_pulses)

# # ok i printed them
# ng is high 3803
# ft is high 3877
# ft is high 3878
# sv is high 3889
# jz is high 3917
  1%|██            
