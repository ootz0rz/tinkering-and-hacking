import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # print("n", n, "queries", queries)

    arr = []
    for _ in range(n):
        arr.append([])

    lastAnswer = 0
    out = []

    for type, x, y in queries:
        idx = (x ^ lastAnswer) % n

        if type == 1:
            arr[idx].append(y)

        if type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            out.append(lastAnswer)

    return out


if __name__ == "__main__":

    def process(s):
        inp = s.strip().split("\n")

        first_multiple_input = inp[0].rstrip().split()

        n = int(first_multiple_input[0])

        q = int(first_multiple_input[1])

        queries = []

        for _ in range(q):
            queries.append(list(map(int, inp[_ + 1].rstrip().split())))

        result = dynamicArray(n, queries)

        print("-----")
        print(s)
        print()
        print("res:")
        print(result)

    process(
        """2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
            """
    )
