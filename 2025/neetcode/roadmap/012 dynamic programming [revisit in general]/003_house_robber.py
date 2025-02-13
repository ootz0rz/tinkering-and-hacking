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

# https://neetcode.io/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def _rob(i, mem):
            if i < 0:
                return 0
            
            if not i in mem:
                mem[i] = max(
                    _rob(i - 1),
                    nums[i] + _rob(i - 2)
                )
            
            return mem[i]

        return _rob(n - 1, {})

        
if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.leastInterval

    check_solution_simple(  
        sf,
        args=[["X","X","Y","Y"], 2],
        expected=5
    )