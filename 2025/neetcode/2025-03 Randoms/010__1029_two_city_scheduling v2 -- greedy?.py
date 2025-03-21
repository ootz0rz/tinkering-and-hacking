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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2

        # this sorting puts us in order such that, for each element
        # one at a time, option "A" is the best option possible since
        # it has the greatest savings compared to option B
        costs.sort(key = lambda x: x[0] - x[1]) # logn

        minCost = 0
        for i in range(n): # n
            minCost += costs[i][0] + costs[i + n][1]
        
        return minCost # nlogn

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.twoCitySchedCost

    check_solution_simple(
        sf,
        args=[[[10,20],[30,200],[400,50],[30,20]]],
        expected=110,
    )


    check_solution_simple(
        sf,
        args=[[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]],
        expected=1859,
    )
