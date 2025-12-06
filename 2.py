import math

from collections import * 
from itertools import * 
from heapq import * 

from tqdm import tqdm
import re



PROD = """
wow"""

TEST = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

x = TEST
# x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
# grid = [list(line) for line in lines]





result = 0


ranges = text.split(",")
invalid_ids = []
for r in ranges:
    a, b = map(int, r.split("-"))
    for id_num in range(a, b + 1):
        id_str = str(id_num)
        length = len(id_str)
        
        found_invalid = False
        found_invalid = re.match(r'^(\d+)\1+$', id_str) is not None

        # for size in range(1, length + 1):
        #     # can we break it?
        #     if length % size != 0:
        #         continue
        #     substrings = [id_str[i:i+size] for i in range(0, length, size)]
        #     ### MUST DO OR BUGGY WITH NUM LENGTH 2 ?????
        #     if len(substrings) <= 1:
        #         continue
        #     if all(sub == substrings[0] for sub in substrings):
        #         print("invalid id", id_num, "sz", size, "range", r)
        #         invalid_ids.append(id_num)
        #         found_invalid = True
        #         break

        if found_invalid:
            invalid_ids.append(id_num)
            continue

result += sum(invalid_ids)

print(result)