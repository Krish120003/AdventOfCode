import math
import collections
from collections import Counter
import re
from tqdm import tqdm
from heapq import heappush, heappop
import heapq

PROD = """
Register A: 46323429
Register B: 0
Register C: 0

Program: 2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0
"""

TEST = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

TEST2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

TEST3 = """
Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0
"""


x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]


A = 0
B = 0
C = 0

register_values, instructions = text.split("\n\n")
register_values = register_values.split("\n")

A, B, C = [int(x.split(":")[1]) for x in register_values]

instructions = [int(x) for x in instructions.strip("Program: ").split(",")]


# The eight instructions are as follows:

# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)

# Here are some examples of instruction operation:

# If register C contains 9, the program 2,6 would set register B to 1.
# If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
# If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
# If register B contains 29, the program 1,7 would set register B to 26.
# If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.


print(A, B, C)
print(instructions)
print(",".join([str(x) for x in instructions]))
print("=" * 20)
target = ",".join([str(x) for x in instructions])


start = 0o6073267275
end = start + (start + 1) * 1000000000
# offset = 1

# # 2,4,1,1,7,5,1,5,4,3,0,3,5,5,3,0
# # 2 =

most_similar = None
most_similar_digit_count = 0

for A in tqdm(range(0, end)):
    temp = A * 8**9 + start
    A = temp
    initial_A = A
    B = 0
    C = 0
    i = 0

    results = []

    while i < len(instructions):
        # print("a", A, B, C)
        ins = instructions[i]
        operand = instructions[i + 1]

        # assert operand != 7

        if operand > 3 and operand < 7:
            combo = A if operand == 4 else B if operand == 5 else C
        else:
            combo = operand

        if ins == 0:
            # print("Dividing A by Combo", A, combo)
            A = A // (2**combo)

        elif ins == 1:
            # print("XORing B with Combo", B, combo)
            B = B ^ operand

        elif ins == 2:
            # print("Modulo 8 of Combo", combo)
            B = combo % 8

        elif ins == 3:
            if A != 0:
                # print("Jumping to", operand, "because A is", A)
                i = operand
                continue
            else:
                ...
                # print("A is 0, not jumping")

        elif ins == 4:
            # print("XORing B with C", B, C)
            B = B ^ C

        elif ins == 5:
            # print("PRINTING COMBO", combo % 8)
            results.append(combo % 8)

        elif ins == 6:
            # print("Dividing A by Combo", A, combo)
            B = A // (2**combo)

        elif ins == 7:
            # print("Dividing A by Combo", A, combo)
            C = A // (2**combo)

        i += 2

    completed_program = ",".join([str(x) for x in results])

    # print(completed_program)
    if completed_program == target:
        print("WHAT")
        print(initial_A)
        print("WHAT")
        # break

    s = 0
    # how many digits are the same?
    for t1, t2 in zip(completed_program, target):
        if t1 == t2:
            s += 1
        else:
            break

    if s > most_similar_digit_count:
        most_similar = initial_A
        most_similar_digit_count = s

        print(most_similar, oct(most_similar), completed_program)


print(target)
# if completed_program == target:
#     print(initial_A)
#     break

# print(f"{A=}, {B=}, {C=}")
# print(",".join([str(x) for x in results]))
