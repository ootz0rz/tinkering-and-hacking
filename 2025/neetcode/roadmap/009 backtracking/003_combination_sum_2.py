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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        n = len(candidates)

        def find(idx, path, sum):
            nonlocal res

            if sum == target:
                res.append(path.copy())
                return 
            
            for i in range(idx, n):
                e = candidates[i]

                # skip previous, this and sorting is key to skip duplicates
                if i > idx and e == candidates[i-1]:
                    continue
                
                si = sum + e
                if si > target:
                    continue

                find(i + 1, path + [e], si)

        find(0, [], 0)

        return res

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.combinationSum2

    check_solution_as_frozensets(
        sf,
        args=[[3], 5],
        expected=[]
    )

    check_solution_as_frozensets(
        sf,
        args=[[9,2,2,4,6,1,5], 8],
        expected=[[1,2,5], [2,2,4], [2,6]]
    )

    check_solution_as_frozensets(
        sf,
        args=[[1,2,3,4,5], 7],
        expected=[[1,2,4], [2,5], [3,4]]
    )


