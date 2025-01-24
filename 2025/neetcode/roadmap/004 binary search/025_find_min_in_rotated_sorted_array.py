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

# https://neetcode.io/problems/find-minimum-in-rotated-sorted-array

'''
[5,6,8,10,20,1,2]

l, mid, r

l = 0, mid = 
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            em = nums[mid]
            er = nums[right]

            if em < er:
                # discard right side
                right = mid
            else:
                # discard left side
                left = mid + 1
        return nums[left]


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findMin

    check_solution_simple(
        sf,
        args=[[3,4,5,6,1,2]],
        expected=1
    )

    check_solution_simple(
        sf,
        args=[[4,5,0,1,2,3]],
        expected=0
    )

    
