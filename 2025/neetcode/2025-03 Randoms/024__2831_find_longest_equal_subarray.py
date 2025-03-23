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

class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 1
        
        d = {}
        for idx,n in enumerate(nums):
            if not n in d:
                d[n] = []
            
            d[n].append(idx)

        print(f"D: {d}")
        
        n = len(nums)

        maxLen = 0
        for val in d:
            print(f"Check Val: {val}")
            i = 0
            j = 0 

            curK = 0
            while i <= j and j < len(d[val]):
                curK = d[val][j] - d[val][i]

                print(f"\tcurK[i:{i}, j:{j}]={curK} vs k: {k} -- max: {maxLen}")
                
                while curK > k and i <= j:
                    print(f"\t\tlower curK[i:{i}, j:{j}]={curK} > k:{k}")
                    curK -= d[val][i + 1] - d[val][i]
                    i += 1
                
                print(f"\t\t => check curK:{curK} <= k:{k}")
                if curK <= k:
                    maxLen = max(maxLen, d[val][j] - d[val][i] + 1)
                
                j += 1

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