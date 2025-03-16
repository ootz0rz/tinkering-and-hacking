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

# ------------ BinaryTree
# stupid...but works
import sys, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from LinkedList import *
# ------------ BinaryTree

# https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # kadane's algo
        curSum = nums[0]
        maxSum = nums[0]

        stopper = len(nums) - 1 # we'll use this to figure out when to stop our circular check
        i = 1 # we already have first element handled above
        while i != stopper: 
            n = nums[i]
        
            cn = curSum + n
            if cn > n:
                curSum = cn
            else:
                curSum = n
                stopper = i
            
            maxSum = max(maxSum, curSum)

            i += 1
            if i >= len(nums):
                i = 0
        
        return maxSum



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.maxSubarraySumCircular

    check_solution_simple(
        sf,
        args=[[5,-3,5]],
        expected=10,
    )