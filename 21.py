import math
import collections
from collections import Counter
import re
from tqdm import tqdm

PROD = """
340A
586A
839A
413A
968A
"""

TEST = """
029A
980A
179A
456A
379A
"""


x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")

# This is the numpad layout
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

# initially we are at A

# controller
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


def get_numpad_directions(code):
    # what are the shortest ways to type out the code using the controller?

    # numpad layout
    numpad = [
        ["7", "8", "9"],  # a
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ]

    # for each key, find the shortest path to each other key.

    dist = 0
    full_path = ""

    curr = (3, 2)  # start at A
    for button_to_press in code:
        # print("Where is", button_to_press, "?")
        # find manhattan dist
        # find the button
        for i in range(4):
            for j in range(3):
                if numpad[i][j] == button_to_press:
                    new = (i, j)
                    break
            else:
                continue
            break

        # print("From", curr, "to", new)

        # navigate from curr to new.
        # we can't touch (3,0)  and we cant go diagonally
        path_to_new = []

        cant_touch = [(3, 0)]

        while curr != new:
            ax, ay = curr
            bx, by = new

            # move in the direction of new
            if ax < bx and (ax + 1, ay) not in cant_touch:
                path_to_new.append("v")
                curr = (ax + 1, ay)
            elif ax > bx and (ax - 1, ay) not in cant_touch:
                path_to_new.append("^")
                curr = (ax - 1, ay)
            elif ay < by and (ax, ay + 1) not in cant_touch:
                path_to_new.append(">")
                curr = (ax, ay + 1)
            elif ay > by and (ax, ay - 1) not in cant_touch:
                path_to_new.append("<")
                curr = (ax, ay - 1)

        # print("Path to new", path_to_new, "for", button_to_press)
        full_path += "".join(path_to_new) + "A"

    return len(full_path), full_path


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
def get_dirpad_paths(seq):
    keypad = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]

    # start at A
    curr = (0, 2)
    full_path = ""

    for button_to_press in seq:
        # find the button
        for i in range(2):
            for j in range(3):
                if keypad[i][j] == button_to_press:
                    new = (i, j)
                    break

        # print("From", curr, "to", new)

        # navigate from curr to new.

        cant_touch = [(0, 0)]

        path_to_new = []
        while curr != new:
            ax, ay = curr
            bx, by = new

            # move in the direction of new
            if ay < by and (ax, ay + 1) not in cant_touch:
                path_to_new.append(">")
                curr = (ax, ay + 1)
            elif ay > by and (ax, ay - 1) not in cant_touch:
                path_to_new.append("<")
                curr = (ax, ay - 1)
            elif ax < bx and (ax + 1, ay) not in cant_touch:
                path_to_new.append("v")
                curr = (ax + 1, ay)
            elif ax > bx and (ax - 1, ay) not in cant_touch:
                path_to_new.append("^")
                curr = (ax - 1, ay)

        # print("Path to new", path_to_new, "for", button_to_press)
        full_path += "".join(path_to_new) + "A"

    return len(full_path), full_path


# result = 0
# # lines = ["379A"]
# # for code in lines:
# #     dist1, path1 = get_numpad_directions(code)
# #     dist2, path2 = get_dirpad_paths(path1)
# #     dist3, path3 = get_dirpad_paths(path2)

# #     print("Numpad:", dist1, path1)
# #     print("Dirpad:", dist2, path2)
# #     print("Dirpad 2:", dist3, path3)

# #     numeric_code = int(code.replace("A", ""))

# #     result += dist3 * numeric_code
# #     print(dist3, "*", numeric_code, "=", dist3 * numeric_code)

# print(result)

from functools import cache


def get_numpad_all_paths(code):
    numpad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None, "0", "A"],
    ]

    @cache
    def find_paths(current_pos, target_pos, current_path=""):
        # we can never go over (3,0)
        if current_pos == (3, 0):
            return []

        if current_pos == target_pos:
            return [current_path]

        ax, ay = current_pos
        bx, by = target_pos
        all_paths = []

        if ax < bx:
            all_paths.extend(find_paths((ax + 1, ay), target_pos, current_path + "v"))
        if ax > bx:
            all_paths.extend(find_paths((ax - 1, ay), target_pos, current_path + "^"))
        if ay < by:
            all_paths.extend(find_paths((ax, ay + 1), target_pos, current_path + ">"))
        if ay > by:
            all_paths.extend(find_paths((ax, ay - 1), target_pos, current_path + "<"))

        return all_paths

    all_full_paths = []
    curr = (3, 2)  # start at A

    for button_to_press in code:
        for i in range(4):
            for j in range(3):
                if numpad[i][j] == button_to_press:
                    new = (i, j)
                    break
            else:
                continue
            break

        paths_to_new = find_paths(curr, new)
        curr = new

        if not all_full_paths:
            all_full_paths = [e + "A" for e in paths_to_new]
            continue
        temp = []
        for path in paths_to_new:
            for prefix in all_full_paths:
                temp.append(prefix + path + "A")
        all_full_paths = temp

    return all_full_paths


@cache
def find_paths_dirpad(current_pos, target_pos, current_path=""):

    # we can never go over (0,0)
    if current_pos == (0, 0):
        return []

    if current_pos == target_pos:
        return [current_path]

    ax, ay = current_pos
    bx, by = target_pos
    all_paths = []

    if ax < bx:
        all_paths.extend(
            find_paths_dirpad((ax + 1, ay), target_pos, current_path + "v")
        )
    if ax > bx:
        all_paths.extend(
            find_paths_dirpad((ax - 1, ay), target_pos, current_path + "^")
        )
    if ay < by:
        all_paths.extend(
            find_paths_dirpad((ax, ay + 1), target_pos, current_path + ">")
        )
    if ay > by:
        all_paths.extend(
            find_paths_dirpad((ax, ay - 1), target_pos, current_path + "<")
        )

    min_len = min(len(p) for p in all_paths)
    all_paths = [p for p in all_paths if len(p) == min_len]

    return all_paths


@cache
def get_dirpad_all_paths(seq):
    keypad = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]

    all_full_paths = []
    curr = (0, 2)  # start at A

    for button_to_press in seq:
        for i in range(2):
            for j in range(3):
                if keypad[i][j] == button_to_press:
                    new = (i, j)
                    break
            else:
                continue
            break

        paths_to_new = find_paths_dirpad(curr, new)
        curr = new

        if not all_full_paths:
            all_full_paths = [e + "A" for e in paths_to_new]
            continue

        temp = []
        for path in paths_to_new:
            for prefix in all_full_paths:
                temp.append(prefix + path + "A")
        all_full_paths = temp[:5]

    return all_full_paths


# print(get_numpad_all_paths("379A"))
# print([get_dirpad_paths(x) for x in get_numpad_all_paths("379A")])


result = 0


def cleanup_path(t):
    return "A".join(["".join(sorted(e)) for e in t.split("A")])


import random


@cache
def find_key_index(k):
    keypad = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]
    for i in range(2):
        for j in range(3):
            if keypad[i][j] == k:
                return (i, j)
                break
        else:
            continue
        break


@cache
def dirpad_min_press(seq, d):
    # if we dont have any more dirpads to press
    if d == 0:
        return len(seq)

    total_presses = 0

    # the total number of presses for this seq is the shortest
    # path from each key to each next key

    # we always start at A
    starting_seq = "A" + seq

    for key, next_key in zip(starting_seq, seq):
        # find the shortest path from key to next_key
        # this is the number of presses
        paths = find_paths_dirpad(find_key_index(key), find_key_index(next_key))

        # for each of these paths which one would take the least amount of presses all the way down the stack?
        stack_pressses = []
        for p in paths:
            path_to_check = p + "A"  # we need the dirpad controlling this one to
            # press all the keys in this one's path, plus an A to confirm

            stack_pressses.append(dirpad_min_press(path_to_check, d - 1))
        min_presses = min(dirpad_min_press(p + "A", d - 1) for p in paths)

        total_presses += min_presses

        # for each of these paths, keep the shorteset

    return total_presses


for code in lines:
    paths = get_numpad_all_paths(code)
    min_dist_in_paths1 = min(len(p) for p in paths)

    # for step in range(25):
    #     print(step)

    #     temp_path = []
    #     for p in tqdm(paths):
    #         temp_path.extend(get_dirpad_all_paths(p))
    #         if len(temp_path) > 1000:
    #             break

    #     min_path = min(temp_path, key=len)
    #     temp_path = [cleanup_path(p) for p in temp_path if len(p) == len(min_path)]
    #     # paths = [min_path]
    #     paths = temp_path

    #     # temp_path = set(temp_path)

    #     # min_dist_in_temp_path = min(len(p) for p in temp_path)

    #     # paths = [p for p in temp_path if len(p) == min_dist_in_temp_path]

    min_dist = min(dirpad_min_press(p, 25) for p in paths)

    numeric_code = int(code.replace("A", ""))

    result += min_dist * numeric_code
    print(min_dist, "*", numeric_code, "=", min_dist * numeric_code)

print(result)
