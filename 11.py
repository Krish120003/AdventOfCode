import math
import collections
from collections import Counter
import re
from tqdm import tqdm

PROD = """
1 24596 0 740994 60 803 8918 9405859
"""

TEST = """
125 17
"""

TEST2 = """
"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]

numssss = text.split()
numssss = [int(x) for x in numssss]


s = 0


seen = set()


# for num in numssss:
#     curr = [num]

#     for _ in tqdm(range(25)):
#         new = []
#         for num in curr:
#             # print(new)
#             if num == 0:
#                 new.append(1)

#             elif len(str(num)) % 2 == 0:
#                 left = str(num)[: len(str(num)) // 2]
#                 right = str(num)[len(str(num)) // 2 :]
#                 new.append(int(left))
#                 new.append(int(right))

#             else:
#                 new.append(num * 2024)

#         for n in new:
#             if n in seen:
#                 print("SEEN THIS BEFORE", n)
#             seen.add(n)

#         curr = new


#     s += len(curr)


from functools import cache


@cache
def process_number(num, depth=75):
    if depth == 0:
        return 1

    if num == 0:
        return process_number(1, depth - 1)

    if len(str(num)) % 2 == 0:
        left = str(num)[: len(str(num)) // 2]
        right = str(num)[len(str(num)) // 2 :]
        return process_number(int(left), depth - 1) + process_number(
            int(right), depth - 1
        )

    return process_number(num * 2024, depth - 1)


for num in numssss:
    results = process_number(num)
    # print(results)
    s += results

print(s)
# print(len(nums))
