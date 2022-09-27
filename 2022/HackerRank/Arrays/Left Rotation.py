import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#


def rotateLeft(d, arr):
    n = len(arr)
    d = d % n  # don't do extra work

    num_swaps = 0
    sidx = 0
    while num_swaps < n:
        cidx = sidx
        last = arr[cidx]

        while True:
            didx = (cidx - d) % n
            temp = arr[didx]
            arr[didx] = last
            last = temp

            cidx = didx

            num_swaps = num_swaps + 1

            if didx == sidx:
                break

        sidx = sidx + 1

    return arr


def d(L, d, j):
    print("-", (j - d) % L, "+", (j + d) % L)


if __name__ == "__main__":

    def process(d, a):
        print(d, a, rotateLeft(d, a))

    process(0, [1, 2, 3, 4, 5, 6])
    process(1, [1, 2, 3, 4, 5, 6])
    process(2, [1, 2, 3, 4, 5, 6])
    process(3, [1, 2, 3, 4, 5, 6])
    process(4, [1, 2, 3, 4, 5, 6])
    process(5, [1, 2, 3, 4, 5, 6])
