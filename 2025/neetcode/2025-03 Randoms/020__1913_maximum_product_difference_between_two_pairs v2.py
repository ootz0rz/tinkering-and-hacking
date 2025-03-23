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

# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

'''
Idea:

Sort, take first two and last two as product pairs
'''
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        maxVals = [0, 0] # largest, 2nd
        minVals = [999999, 999999] # smallest, 2nd

        for n in nums:
            
            if n > maxVals[0]:
                maxVals[1] = maxVals[0]
                maxVals[0] = n
            elif n > maxVals[1]:
                maxVals[1] = n

            if n < minVals[0]:
                minVals[1] = minVals[0]
                minVals[0] = n
            elif n < minVals[1]:
                minVals[1] = n
        
        return (maxVals[0] * maxVals[1]) - (minVals[0] * minVals[1])
            

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.longestWPI

    check_solution_simple(
        sf,
        args=[[9,9,6,0,6,6,9]],
        expected=3,
    )

    check_solution_simple(
        sf,
        args=[[6,6,9]],
        expected=1,
    )