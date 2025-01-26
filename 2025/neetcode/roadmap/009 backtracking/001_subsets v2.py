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

# https://neetcode.io/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:       
        subs = [[]] #key: have to seed with empty set
        n = len(nums)

        for num in nums:
            r = []

            for s in subs:
                r.append(s + [num])

            subs.extend(r) 

        return subs
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.subsets

    check_solution_as_frozensets(
        sf,
        args=[[]],
        expected=[[]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[0]],
        expected=[[], [0]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[0,1]],
        expected=[[], [0], [1], [0,1]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[1,2,3]],
        expected=[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    )    