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

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            m = L + ((R - L) // 2)

            if nums[m] == target:
                return m
            
            # figure out if the target is in left half or right half...
            if target < nums[m]:
                # check left side first
                if nums[L] < target:
                    # nums[L] < target < nums[m] => our target is in [L:m]
                    R = m - 1
                else:
                    # nums[L] > target < nums[m] => our target can't be in left side
                    L = m + 1
            else: # target >= nums[m]
                # check right side in same way
                if nums[R] < target:
                    # nums[R] < target >= nums[m] 
                    R = m - 1
                else:
                    # nums[R] >= target >= nums[m] => nums[m] < target < nums[R] => target in [m:R]
                    L = m + 1
        
        return -1


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.search

    check_solution_simple(
        sf,
        args=[[4,5,6,7,0,1,2], 0],
        expected=4,
    )