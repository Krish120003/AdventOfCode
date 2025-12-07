import math
import collections
from collections import Counter
import re
from tqdm import tqdm


TEST = """

"""

PROD = """

"""

x = TEST
# x = PROD
x = x.strip("\n")

# Data in differnt formats for quick access
text = x
lines = x.split("\n")
grid = [list(line) for line in lines]

result = 0


print(result)
