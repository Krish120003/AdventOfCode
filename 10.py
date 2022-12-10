from math import *
from itertools import *
from fractions import *
from string import *
from copy import *
from collections import *

# You avoid the ropes, plunge into the river, and swim to shore.

# The Elves yell something about meeting back up with them upriver, but the river is too loud to tell exactly what they're saying. They finish crossing the bridge and disappear from view.

# Situations like this must be why the Elves prioritized getting the communication system on your handheld device working. You pull it out of your pack, but the amount of water slowly draining from a big crack in its screen tells you it probably won't be of much immediate use.

# Unless, that is, you can design a replacement for the device's video system! It seems to be some kind of cathode-ray tube screen and simple CPU that are both driven by a precise clock circuit. The clock circuit ticks at a constant rate; each tick is called a cycle.

# Start by figuring out the signal being sent by the CPU. The CPU has a single register, X, which starts with the value 1. It supports only two instructions:

# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.
# The CPU uses these instructions in a program (your puzzle input) to, somehow, tell the screen what to draw.

# Consider the following small program:

# noop
# addx 3
# addx -5
# Execution of this program proceeds as follows:

# At the start of the first cycle, the noop instruction begins execution. During the first cycle, X is 1. After the first cycle, the noop instruction finishes execution, doing nothing.
# At the start of the second cycle, the addx 3 instruction begins execution. During the second cycle, X is still 1.
# During the third cycle, X is still 1. After the third cycle, the addx 3 instruction finishes execution, setting X to 4.
# At the start of the fourth cycle, the addx -5 instruction begins execution. During the fourth cycle, X is still 4.
# During the fifth cycle, X is still 4. After the fifth cycle, the addx -5 instruction finishes execution, setting X to -1.
# Maybe you can learn something by looking at the value of the X register throughout execution. For now, consider the signal strength (the cycle number multiplied by the value of the X register) during the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

# For example, consider this larger program:

# addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop
# The interesting signal strengths can be determined as follows:

# During the 20th cycle, register X has the value 21, so the signal strength is 20 * 21 = 420. (The 20th cycle occurs in the middle of the second addx -1, so the value of register X is the starting value, 1, plus all of the other addx values up to that point: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4 = 21.)
# During the 60th cycle, register X has the value 19, so the signal strength is 60 * 19 = 1140.
# During the 100th cycle, register X has the value 18, so the signal strength is 100 * 18 = 1800.
# During the 140th cycle, register X has the value 21, so the signal strength is 140 * 21 = 2940.
# During the 180th cycle, register X has the value 16, so the signal strength is 180 * 16 = 2880.
# During the 220th cycle, register X has the value 18, so the signal strength is 220 * 18 = 3960.
# The sum of these signal strengths is 13140.

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?


TEST = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

PROD = """
addx 1
addx 4
addx -2
addx 3
addx 3
addx 1
noop
addx 5
noop
noop
noop
addx 5
addx 2
addx 3
noop
addx 2
addx 4
noop
addx -1
noop
addx 3
addx -10
addx -17
noop
addx -3
addx 2
addx 25
addx -24
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 14
addx -9
noop
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -5
noop
noop
addx -19
addx -11
addx 5
addx 3
noop
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 4
noop
noop
addx 5
noop
noop
noop
addx 5
addx -3
addx 8
noop
addx -15
noop
addx -12
addx -9
noop
addx 6
addx 7
addx -6
addx 4
noop
noop
noop
addx 4
addx 1
addx 5
addx -11
addx 29
addx -15
noop
addx -12
addx 17
addx 7
noop
noop
addx -32
addx 3
addx -8
addx 7
noop
addx -2
addx 5
addx 2
addx 6
addx -8
addx 5
addx 2
addx 5
addx 17
addx -12
addx -2
noop
noop
addx 7
addx 9
addx -8
addx 2
addx -33
addx -1
addx 2
noop
addx 26
addx -22
addx 19
addx -16
addx 8
addx -1
addx 3
addx -2
addx 2
addx -17
addx 24
addx 1
noop
addx 5
addx -1
noop
addx 5
noop
noop
addx 1
noop
noop
"""

# x = TEST
x = PROD

data = x.strip().split("\n")


cycles = 0
X = 1
strength = 0

# It seems like the X register controls the horizontal position of a sprite. Specifically, the sprite is 3 pixels wide, and the X register sets the horizontal position of the middle of that sprite. (In this system, there is no such thing as "vertical position": if the sprite's horizontal position puts its pixels where the CRT is currently drawing, then those pixels will be drawn.)

# You count the pixels on the CRT: 40 wide and 6 high. This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on. The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.

# Like the CPU, the CRT is tied closely to the clock circuit: the CRT draws a single pixel during each cycle. Representing each pixel of the screen as a #, here are the cycles during which the first and last pixel in each row are drawn:

# Cycle   1 -> ######################################## <- Cycle  40
# Cycle  41 -> ######################################## <- Cycle  80
# Cycle  81 -> ######################################## <- Cycle 120
# Cycle 121 -> ######################################## <- Cycle 160
# Cycle 161 -> ######################################## <- Cycle 200
# Cycle 201 -> ######################################## <- Cycle 240
# So, by carefully timing the CPU instructions and the CRT drawing operations, you should be able to determine whether the sprite is visible the instant each pixel is drawn. If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

# Render the image given by your program. What eight capital letters appear on your CRT?


currentCRTLine = ""

for index, i in enumerate(data):
    if i.startswith("addx"):

        # after the first cycle, add 1
        cycles += 1

        # print(cycles, X, strength)

        if len(currentCRTLine) in (X-1, X, X+1):
            currentCRTLine += "#"
        else:
            currentCRTLine += "."

        if cycles % 40 == 0:
            print(currentCRTLine)
            currentCRTLine = ""

        # done 2 cycles
        cycles += 1
        if len(currentCRTLine) in (X-1, X, X+1):
            currentCRTLine += "#"
        else:
            currentCRTLine += "."

        if cycles % 40 == 0:
            print(currentCRTLine)
            currentCRTLine = ""

        X += int(i.split(" ")[1])

    elif i.startswith("noop"):
        cycles += 1
        if len(currentCRTLine) in (X-1, X, X+1):
            currentCRTLine += "#"
        else:
            currentCRTLine += "."

        if cycles % 40 == 0:
            print(currentCRTLine)
            currentCRTLine = ""

        if cycles in [40, 80, 120, 160, 200, 240]:
            # print(cycles, X, strength)
            strength += X * cycles
