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

# https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n # avoid large k

        # reverse entire array
        def _rev(l, r):
            nonlocal nums

            while l < r:
                t = nums[l] 
                nums[l] = nums[r]
                nums[r] = t

                l += 1
                r -= 1
        
        _rev(0, n - 1)
        print(f"Rev: {nums}")

        _rev(0, k)
        print(f"Rev <k: {nums}")
        
        _rev(k + 1, n - 1)
        print(f"Rev >k: {nums}")

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.rotate

    check_solution_simple(  
        sf,
        args=[[1,2,3,4,5,6,7], 3],
        expected=0
    )