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

# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        l = 0
        minLen = math.inf
        curSum = 0
        for r, re in enumerate(nums):
            curSum += re

            while curSum >= target and l <= r:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
        
        return minLen if minLen != math.inf else 0


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.twoSum

    check_solution_simple(  
        sf,
        args=[[2,7,11,15], 9],
        expected=[1, 2]
    )
