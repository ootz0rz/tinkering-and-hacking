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
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)

        chosen = [False] * n

        def find(path):
            nonlocal res

            if len(path) == len(nums):
                res.append(path)
                return

            for i in range(0, n):
                if chosen[i]:
                    continue
                
                chosen[i] = True
                find(path + [nums[i]])
                chosen[i] = False

        find([])
                
        return res

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.permute

    check_solution_as_frozensets(
        sf,
        args=[[3]],
        expected=[[3]]
    )

    check_solution_as_tuplesets(
        sf,
        args=[[1,2,3]],
        expected=[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    )


