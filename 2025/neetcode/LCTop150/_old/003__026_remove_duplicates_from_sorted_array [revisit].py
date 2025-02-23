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

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

'''
Idea:

We sweep through nums with j

If j == i, then we continue to increment j
If j != i, then we copy n[i] = n[j] and increment both
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0

        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
                i = i + 1
            j = j + 1
        return i

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