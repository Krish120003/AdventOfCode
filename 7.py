from collections import defaultdict
from collections import Counter
import math
import itertools
import collections
from icecream import ic

from random import shuffle


def is_number(x):
    try:
        int(x)
        return True
    except:
        return False


# from tqdm import tqdm

TEST = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
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


# its kinda like poker
# Every hand is exactly one type. From strongest to weakest, they are:
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
# Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

# we have to sort them lol

# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order
strenghts = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": -10,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def sorter(x):
    cards = x.split(" ")[0]
    cards_set = set(cards)
    # check what type of hand it is

    cards_ranked = [1000 - strenghts[c] for c in cards]

    if len(cards_set) == 1:
        # all cards are the same
        return 0, *cards_ranked

    if len(cards_set) == 2:
        c = Counter(cards)
        # if we have 4, then there is a 4 of a kind
        if 4 in c.values():
            # if we have 4 J's or 1 J, then we have a 5 of a kind
            if "J" in c:
                return 0, *cards_ranked
            return 1, *cards_ranked
        # full house, (3 of a kind and 2 of a kind)
        if 3 in c.values():
            # if we have 3 J's or 2 J's, then we have a 5 of a kind
            if "J" in c:
                return 0, *cards_ranked
            return 2, *cards_ranked

    if len(cards_set) == 3:
        # 3 of a kind and 2 different cards
        c = Counter(cards)
        if 3 in c.values():
            # if we have 1 J or 3 J's, then we have a 4 of a kind
            # HOPEFULLY THIS IS RGHT
            if "J" in c:
                return 1, *cards_ranked
            return 3, *cards_ranked
        # 2 pairs of 2 different cards, and 1 different card
        if 2 in c.values():
            if "J" in c:
                if c["J"] == 2:
                    # 2 pairs, one of the pairs is J so we have a 4 of a kind
                    return 1, *cards_ranked
                else:
                    # 2 pairs, only 1 card is J, so we have a full house
                    return 2, *cards_ranked

            # 2 pairs, none of the pairs is J, so we have a 2 pair
            return 4, *cards_ranked

    if len(cards_set) == 4:
        # 2 cards are same and the rest are different, so
        # lets make those 2 cards into 3 and have 3 different cards, three of a kind
        if "J" in cards_set:
            return 3, *cards_ranked
        # 1 pair
        return 5, *cards_ranked

    # high card
    if "J" in cards_set:
        return 5, *cards_ranked
    return 6, *cards_ranked
    # wow this is so confusing aklsdfjljaksjdfaslkdfjalsdjk


lines.sort(key=sorter, reverse=True)


res = 0
for i, l in enumerate(lines):
    res += (i + 1) * int(l.split(" ")[1])
    ic(i + 1, l)

print(res)
