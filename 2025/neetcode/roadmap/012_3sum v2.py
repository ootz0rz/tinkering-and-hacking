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

# https://neetcode.io/problems/three-integer-sum
# https://leetcode.com/problems/3sum/description/
'''
Another way to think of this is to divide it into diff sets of numbers

Our input array will consist of either negative numbers, 0s, or positive numbers.
We want to find all the pairings that result in a final value of 0

Since the final value must be 0, the possible 3-set outputs can be one of the following:

    - (0,0,0) [[0]]
    - (neg, 0, -neg) => (neg, 0, pos) where pos = -neg [[1]]
    - (neg, neg, pos) [[2]]
    - (neg, pos, pos) [[3]]

We can count the number of 0s and divide into several cases:
    - If we have 3 or more zeroes, one of our final answers must be (0,0,0) [[A]]
    - If we have 1 or 2 zeroes, we should find every possible (neg, 0, -neg) set [[B]]
    - Finally we do the default set of (neg, neg, pos) or (neg, pos, pos) [[C]]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negs = defaultdict([])
        poss = defaultdict([])
        numZero = 0
        res = []

        for idx, e in enumerate(nums):
            if e == 0:
                numZero += 1
            elif e > 0:
                poss[e].add(idx)
            else:
                negs[e].add(idx)
        
        if numZero > 0: # [[B]]

            if numZero >= 3: # [[A]] -> [[0]]
                res.append([0,0,0])

            # [[1]]
            for n in negs:
                if (-n) in poss:
                    res.append(n, 0, -n)
        
        # [[C]]
        nlist = negs.keys()
        plist = poss.keys()

        # [[2]] for each pos number, find 2 negative numbers

            
        

        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.threeSum

    check_solution_as_tuplesets(
        sf,
        args=[[0,0,0]],
        expected=[[0,0,0]]
    )

    check_solution_as_tuplesets(
        sf,
        args=[[0,1,1]],
        expected=[]
    )

    check_solution_as_tuplesets(
        sf,
        args=[[-1,0,1,2,-1,-4]],
        expected=[[-1,-1,2],[-1,0,1]]
    )