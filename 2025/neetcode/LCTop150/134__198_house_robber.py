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

# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}

        def rob(i):
            nonlocal m
            if i >= len(nums):
                return 0

            if not i in m:
                m[i] = max(
                    # either we rob current house + the nextnext one over
                    nums[i] + rob(i + 2), 

                    # or we rob the next house and skip this one
                    rob(i + 1)
                )
            
            return m[i]

        return max(rob(0), rob(1))

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.rob

    check_solution_simple(
        sf,
        args=[[1,2,3,1]],
        expected=4,
    )
