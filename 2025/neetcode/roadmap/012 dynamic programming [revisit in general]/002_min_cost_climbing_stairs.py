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

# https://neetcode.io/problems/min-cost-climbing-stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def _getMin(idx, mem):
            nonlocal cost, n

            if idx >= n:
                return 0 # no cost to go to yourself
            
            if not idx in mem:
                mem[idx] = cost[idx] + min(_getMin(idx + 1, mem), _getMin(idx + 2, mem))

            return mem[idx]

        m = {}
        return min(_getMin(0, m), _getMin(1, m))

        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.leastInterval

    check_solution_simple(  
        sf,
        args=[["X","X","Y","Y"], 2],
        expected=5
    )