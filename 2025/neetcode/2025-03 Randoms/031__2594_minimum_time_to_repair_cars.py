from typing import List,Optional
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/minimum-time-to-repair-cars/

'''
We can set an upper bound for our time to repair by putting all the
cars on our fastest repair-man

And then we can binary search from there to see if we can still repair
all the cars as needed.

R*n^2 = t

If we rearrange this for n to determine number of possible repairs by
a single repairman in a given timespan, we get:

n = sqrt(t / R)

We can use this for all our repairman for each search of T to see if
repair is feasible.
'''
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        maxTime = float('inf')
        for r in ranks:
            maxTime = min(r * cars * cars, maxTime)

        def calcMax(time):
            nonlocal ranks

            maxCars = 0
            for r in ranks:
                maxCars += int(math.sqrt(time // r))
            
            return maxCars
        
        i = 1
        j = maxTime
        while i < j:
            print(f"i:{i} <= j:{j}")
            mid = i + ((j - i) // 2)

            maxCars = calcMax(mid)

            print(f"\tMax Cars: {maxCars}")

            if maxCars >= cars:
                j = mid
            else:
                i = mid + 1
        
        print(f"END: {i}, {j}")

        return i
                


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.repairCars

    check_solution_simple(
        sf,
        args=[[4,2,3,1], 10],
        expected=16,
    )
