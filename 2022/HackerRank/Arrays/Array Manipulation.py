# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true
import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for a, b, k in queries:
        arr[a - 1] = arr[a - 1] + k
        arr[b] = arr[b] - k

    maxval = 0
    run = 0

    for e in arr:
        run = run + e
        if run > maxval:
            maxval = run

    return maxval
