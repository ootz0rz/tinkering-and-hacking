from typing import List
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

# https://neetcode.io/problems/eating-bananas

'''
Since piles.len <= h <= ... we know, that in the worst case, we'd need to eat
max(piles) bananas per hour.

Ex: piles = [1,1,100,1,1], h = 5, we'd need to eat 100 bananas per hour. We can
    only eat a single pile per hour, and the largest one has 100, but we have
    5 piles, so we must be able to consume that largest pile within 1 hour in
    order to have enough time to finish the rest.

This means that the fastest speed we ever need is max(piles) per hour.

Ex2: piles = [4,4,4], h = 10, we'd need 2 bananas per hour since 6 << h=10, 
    but if we did only 1, 12 >> h=10

We can find the largest number O(n), then do a binary search from [1, max(piles)]
to find the smallest value R (rate of consumption per hour) such that we can 
consume all the piles within `h` hours. => O(n * log[max(piles)])
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        minBananasPerHour = right

        # search [1, right]
        while left <= right:
            mid = left + ((right - left) // 2)

            totalTime = 0
            for e in piles:
                totalTime += math.ceil(float(e) / mid)
            
            if totalTime <= h:
                minBananasPerHour = mid

                # discard right
                right = mid - 1
            else:
                left = mid + 1
        
        return minBananasPerHour
            



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.searchMatrix

    check_solution_simple(
        sf,
        args=[[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10],
        expected=True
    )

    check_solution_simple(
        sf,
        args=[[[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15],
        expected=False
    )

    
