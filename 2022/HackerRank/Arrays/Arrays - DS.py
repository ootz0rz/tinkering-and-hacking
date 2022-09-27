# https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def reverseArray(a):
    i = 0
    j = len(a) - 1

    t = None
    while i < j:
        t = a[i]
        a[i] = a[j]
        a[j] = t

        i = i + 1
        j = j - 1

    return a


if __name__ == "__main__":
    print([], reverseArray([]))
    print([0], reverseArray([0]))
    print([0, 1], reverseArray([0, 1]))
    print([0, 1, 2, 3], reverseArray([0, 1, 2, 3]))
    print([0, 1, 2, 3, 4], reverseArray([0, 1, 2, 3, 4]))
