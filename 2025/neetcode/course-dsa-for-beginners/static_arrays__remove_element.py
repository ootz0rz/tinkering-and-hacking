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

class Solution:
    # https://leetcode.com/problems/remove-element/description/
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)

        if l == 0:
            return 0
        
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left = left + 1
        
        return left

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.removeElement

    check_solution_simple(
        sf,
        args=[[3,2,2,3], 3],
        expected=2
    )

    check_solution_simple(
        sf,
        args=[[0,1,2,2,3,0,4,2], 2],
        expected=5
    )