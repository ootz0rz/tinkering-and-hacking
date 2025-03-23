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

# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        lookup = defaultdict(int)
        for n in nums:
            lookup[abs(n)] += 1

        numPairs = 0
        for key in lookup:
            if k > 0 and (k + key) in lookup:
                numPairs += 1
            elif k == 0 and lookup[key] > 1:
                numPairs += 1
        
        return numPairs

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findPairs

    check_solution_simple(
        sf,
        args=[[3,1,4,1,5], 2],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5], 1],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[1,3,1,5,4], 0],
        expected=1,
    )