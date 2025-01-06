from typing import List
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

# https://neetcode.io/problems/trapping-rain-water
# https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    '''
    For each idx i, compute prefix max, and compute postfix max

    Then we know that at any given index i, the max water we can store is... 
        If prefix max > i, and postfix max > i:
            water[i] = min(prefix[i], postfix[i]) - height[i]
    '''
    def trap(self, height: List[int]) -> int:
        L = len(height)

        if L == 0:
            return 0

        prefix = [0] * L
        postfix = [0] * L

        maxWater = 0

        # build prefix max height for each i
        for i in range(1, L):
            prefix[i] = max(prefix[i - 1], height[i - 1])

        for i in range(L - 2, -1, -1):
            postfix[i] = max(postfix[i + 1], height[i + 1])

        # for each i, check how much water we can store and add it all together
        for idx in range(L):
            maxWater += max(0, min(prefix[idx], postfix[idx]) - height[idx])

        return maxWater

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.maxArea

    check_solution_simple(
        sf,
        args=[[1,1]],
        expected=1
    )

    check_solution_simple(
        sf,
        args=[[1,7,2,5,4,7,3,6]],
        expected=36
    )

    check_solution_simple(
        sf,
        args=[[2,2,2]],
        expected=4
    )

    check_solution_simple(
        sf,
        args=[[1,8,6,2,5,4,8,3,7]],
        expected=49
    )