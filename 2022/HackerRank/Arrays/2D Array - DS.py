import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

HOURGLASS_DEF = [
    # first row
    [0, 0],
    [0, 1],
    [0, 2],
    # mid
    [1, 1],
    # bot
    [2, 0],
    [2, 1],
    [2, 2],
]


def hourglassSum(arr):
    global HOURGLASS_DEF
    biggest = None

    M = len(arr)
    N = len(arr[0])

    i = 0
    while i <= (M - 3):
        j = 0
        while j <= (N - 3):
            sum = 0

            for x, y in HOURGLASS_DEF:
                sum = sum + arr[i + x][j + y]

            if biggest is None or sum >= biggest:
                biggest = sum

            j = j + 1
        i = i + 1

    return biggest


if __name__ == "__main__":
    a = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    print(a)
    print(hourglassSum(a))

    b = """0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7
    """
