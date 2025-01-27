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

# https://neetcode.io/problems/combination-target-sum-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        n = len(nums)
        def find(idx, path):
            nonlocal res

            res.append(path)

            for i in range(idx, n):
                # skip dupes
                if i > idx and nums[i] == nums[i-1]:
                    continue
                
                find(i + 1, path + [nums[i]])

        find(0, [])

        return res

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.subsetsWithDup

    check_solution_as_frozensets(
        sf,
        args=[[]],
        expected=[[]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[1]],
        expected=[[], [1]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[1, 2]],
        expected=[[], [1], [2], [1, 2]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[1,2,1]],
        expected=[[],[1],[1,2],[1,1],[1,2,1],[2]]
    )


