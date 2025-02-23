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

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

'''
Idea:

We sweep through nums with j

If j == i, then we continue to increment j
If j != i, then we copy n[i] = n[j] and increment both
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1
        count = 0

        while right < len(nums):
            if nums[left - count] == nums[right]:
                nums[left] = nums[right]
                left += 1 
                count += 1
            else:
                nums[left] = nums[right]
                count = 0

            right += 1

        return left

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.coinChange

    check_solution_simple(  
        sf,
        args=[[1], 0],
        expected=0
    )

    check_solution_simple(  
        sf,
        args=[[1], 5],
        expected=5
    )

    check_solution_simple(  
        sf,
        args=[[5], 5],
        expected=1
    )

    check_solution_simple(  
        sf,
        args=[[1,5], 10],
        expected=2
    )

    check_solution_simple(  
        sf,
        args=[[1, 5], 12],
        expected=4
    )