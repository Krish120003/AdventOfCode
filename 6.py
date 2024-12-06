import math
import collections
from collections import Counter
import re


TEST = """

"""

PROD = """

"""

x = TEST
x = PROD
x = x.strip()

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]
