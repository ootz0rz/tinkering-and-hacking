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

'''
Idea:

We'll traverse the list backwards, and modify each cell in place to write the min value to reach the end

Then we just have to give the min cost of first 2 elements, which will incorporate everything after it anyways
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

        
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