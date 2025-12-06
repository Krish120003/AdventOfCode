import math

from collections import * 
from itertools import combinations
from heapq import * 

from tqdm import tqdm
import re



PROD = """
wow
"""

TEST = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
# grid = [list(line) for line in lines]

from functools import cache


# this too slow
def max_k_number(line, curr_number="", curr_index=0, memo={}):
    if len(curr_number) == 12:
        return curr_number
    
    if curr_index >= len(line):
        return "-1"
    
    if (curr_number, curr_index) in memo:
        return memo[(curr_number, curr_index)]
    
    number_if_choose_current = int(max_k_number(line, curr_number + line[curr_index], curr_index + 1))
    number_if_skip_current = int(max_k_number(line, curr_number, curr_index + 1))

    result =  max(
        int(number_if_choose_current),
        int(number_if_skip_current)
    )

    memo[(curr_number, curr_index)] = result
    return str(result)

# def max_k_number(s: str, k: int = 12) -> str:
#     n = len(s)
#     stack = []
#     canremove = n - k

#     for ch in s:
#         while canremove > 0 and len(stack) > 0 and stack[-1] < ch:
#             stack.pop()
#             canremove -= 1
#         stack.append(ch)
#     result = "".join(stack[:k])
#     return result

total = 0
for line in tqdm(text.splitlines()):
    so_far = int(max_k_number(line))
    total += so_far

print(total)