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

# https://leetcode.com/problems/longest-well-performing-interval/

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # process input, >8 = 1, <= 8 = -1
        for idx in range(len(hours)):
            hours[idx] = 1 if hours[idx] > 8 else -1

        # now find longest subset sum > 0
        counts = defaultdict(int)
        counts[0] = 1 # for first index

        ans = 0
        curr = 0 

        for h in hours:
            curr += h
            ans += counts[curr]
            counts[curr] += 1
        
        return ans

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestWPI

    check_solution_simple(
        sf,
        args=[[9,9,6,0,6,6,9]],
        expected=3,
    )

    check_solution_simple(
        sf,
        args=[[6,6,9]],
        expected=1,
    )