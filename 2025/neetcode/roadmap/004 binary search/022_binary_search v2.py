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

# https://neetcode.io/problems/binary-search

class Solution:
    def _search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = left + ((right - left) // 2)

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            # discard right side
            return self._search(nums, target, left, mid - 1)
        else:
            # discard left side
            return self._search(nums, target, mid + 1, right)

    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target, 0, len(nums) - 1)


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
        args=[[-1,0,2,4,6,8], 4],
        expected=3
    )

    check_solution_simple(
        sf,
        args=[[-1,0,2,4,6,8], 3],
        expected=-1
    )

    
