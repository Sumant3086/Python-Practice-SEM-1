import math
import os
import random
import re
import sys


#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    a = [0]
    b = [0]
    for x in numbers:
        a.append(a[-1] + x)
        b.append(b[-1] + (x == 0))
    return [a[r] - a[l - 1] + x * (b[r] - b[l - 1]) for l, r, x in queries]
    
