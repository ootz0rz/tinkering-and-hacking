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

        leftMax = 0
        rightMax = 0
        allWater = 0

        i = 0
        j = L - 1

        while i < j:
            hi = height[i]
            hj = height[j]

            if hi <= hj:
                if hi >= leftMax:
                    leftMax = hi
                else:
                    allWater += leftMax - hi

                i = i + 1
            else: # hi > hj
                if hj >= rightMax:
                    rightMax = hj
                else:
                    allWater += rightMax - hj
                
                j = j - 1

        return allWater

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.trap

    check_solution_simple(
        sf,
        args=[[0,1,0,2,1,0,1,3,2,1,2,1]],
        expected=6
    )

    check_solution_simple(
        sf,
        args=[[4,2,0,3,2,5]],
        expected=9
    ) 