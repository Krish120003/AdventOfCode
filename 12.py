from collections import defaultdict
from collections import Counter
import math
import itertools
import collections

# from tqdm import tqdm

from icecream import ic


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

PROD = """
"""

with open("input.txt", "r") as f:
    PROD = f.read()

    TEST = TEST.strip()
    PROD = PROD.strip()

x = TEST
# x = PROD

lines = x.split("\n")


import re

count = 0

# from functools import lru_cache


# USELESS FUNCTION
def can_match(target, some_pattern):
    ic(target, some_pattern)

    n = min(
        len(target),
        len(some_pattern),
    )

    for i in range(n):
        if target[i] != some_pattern[i]:
            if some_pattern[i] == "?":
                continue
            else:
                return False

    return True


from tqdm import tqdm

from functools import lru_cache


@lru_cache(maxsize=None)
def resurse_find(springs, groups):
    ic(springs, groups)
    matched = 0

    if not springs:
        # no more chars to match!
        # if we dont have any groups then we are valid match
        return int(len(groups) == 0)

    if springs[0] == ".":
        # ignore the dots
        return resurse_find(springs[1:], groups)

    if springs[0] == "?":
        # well the question can be . or # so lets try both
        # omg this is nice because if some recursion calls this then we can cache this
        matched += resurse_find("." + springs[1:], groups)
        matched += resurse_find("#" + springs[1:], groups)

    if springs[0] == "#":
        # uhhh if we have no groups then we cant match lol
        if len(groups) == 0:
            return 0

        # ok so we have a #, lets see if theres enough of them
        needed = groups[0]

        # do we even have enough chars left to match?
        if needed > len(springs):
            return 0

        # ok so we have enough chars left to match, lets try it
        if "." in springs[:needed]:
            # if we have a dot in the match then we cant match
            return 0

        # ok so we have enough # or ? to match because we dont have any dots
        # but we cant have the next char be a hash as well because groups are contiguuous

        # BUT!!! THE NEXT CHAR MIGHT NOT EVEN EXIST IF WE ARE AT THE END OF THE STRING
        # wait cant we just add a . to the end of the string to make this easier?

        if len(springs) > needed and springs[needed] == "#":
            # if we have a hash next then we cant match
            return 0

        # ok we have match only if the next char is a dot
        matched += resurse_find(springs[needed + 1 :], groups[1:])

    print(matched)
    return matched


for line in tqdm(lines):
    springs, rest = line.split(" ")
    groups = tuple(list(map(int, rest.split(","))) * 5)

    springs = "?".join([springs] * 5) + "."
    count += resurse_find(springs, groups)


print(count)
