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

# https://leetcode.com/problems/find-the-longest-equal-subarray/description/

'''
Idea:

We track the maximum frequency of items in a given range sliding window
If the length of the window - maxFreq > k, then bring up the left of the
window
'''
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        i = 0

        d = defaultdict(int)

        maxLen = 0
        for j in range(n):
            d[nums[j]] += 1

            maxLen = max(maxLen, d[nums[j]])

            if (j - i + 1) - maxLen > k:
                d[nums[i]] -= 1
                i += 1

        return maxLen

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestEqualSubarray

    check_solution_simple(
        sf,
        args=[[], 0],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[1], 5],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[1,1,1,1], 5],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[1,1,1,1], 1],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[1,1,2,2,1,1], 1],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[[1,1,2,2,1,1], 2],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[1,3,2,3,1,3], 3],
        expected=3,
    )