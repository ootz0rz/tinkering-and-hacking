from typing import List, Optional, Self
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

# https://neetcode.io/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr) # O(n)

        # O(log k) since k points max
        for x,y in points:
            val = (x**2) + (y**2)

            # we're gonna use a max heap by negating value, and cap at k
            heapq.heappush(arr, (-val, x, y))
            
            # check if above k
            if len(arr) > k:
                heapq.heappop(arr)

        return [[x, y] for (v, x, y) in arr]
        


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.kClosest

    check_solution_simple(  
        sf,
        args=[[[0,2],[2,2]], 1],
        expected=[[0,2]]
    )

    check_solution_simple(  
        sf,
        args=[[[0,2],[2,0],[2,2]], 2],
        expected=[[0,2],[2,0]]
    )