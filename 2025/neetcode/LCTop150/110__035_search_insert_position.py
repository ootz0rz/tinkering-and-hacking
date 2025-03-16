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
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        L = 0
        R = len(nums) - 1

        while L <= R:
            m = L + ((R - L) // 2)

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                R = m - 1
            else:
                L = m + 1

        return L


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.searchInsert

    check_solution_simple(
        sf,
        args=[[1,3,5,6], 5],
        expected=2,
    )