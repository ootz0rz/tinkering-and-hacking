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
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo
        curSum = nums[0]
        maxSum = nums[0]

        for n in nums[1:]: # we already have first element handled above
            curSum = max(n, curSum + n)
            maxSum = max(maxSum, curSum)
        
        return maxSum



if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.maxSubArray

    check_solution_simple(
        sf,
        args=[[-2,1,-3,4,-1,2,1,-5,4]],
        expected=6,
    )
