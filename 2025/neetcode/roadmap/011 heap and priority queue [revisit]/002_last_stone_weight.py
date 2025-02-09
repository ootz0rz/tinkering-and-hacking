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

# https://neetcode.io/problems/last-stone-weight

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones] # negate to make this function like a max-heap
        heapq.heapify(h) 

        while len(h) > 1: # need at least 2 left...
            s1 = heapq.heappop(h)
            s2 = heapq.heappop(h)

            if s1 != s2:
                heapq.heappush(h, s1 - s2)

        h.append(0)
        return -h[0]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.lastStoneWeight

    check_solution_simple(  
        sf,
        args=[3, [[0,1], [0,2]]],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[6, [[0,1], [1,2], [2,3], [4,5]]],
        expected=2
    )