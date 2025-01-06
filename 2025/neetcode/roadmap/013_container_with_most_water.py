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

# https://neetcode.io/problems/max-water-container
# https://leetcode.com/problems/container-with-most-water/
class Solution:
    '''
    Idea is to use 2 pointer, starting from either end... track volume, and then push the smaller bar inwards and see if we hold more?
    '''
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            ei = heights[i]
            ej = heights[j]

            biggest = max(biggest, min(ei, ej) * (j - i))

            if ei > ej:
                j = j - 1
            else:
                i = i + 1
        
        return biggest

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
        args=[[0,0,0]],
        expected=[[0,0,0]]
    )

    check_solution_simple(
        sf,
        args=[[0,1,1]],
        expected=[]
    )

    check_solution_simple(
        sf,
        args=[[-1,0,1,2,-1,-4]],
        expected=[[-1,-1,2],[-1,0,1]]
    )