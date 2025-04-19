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

# https://leetcode.com/problems/distinct-numbers-in-each-subarray/

class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        
        i = 0
        j = 0

        # process first k numbers
        seen = defaultdict(int)
        while j != k and j < len(nums):
            seen[nums[j]] += 1

            j += 1
        
        res = []
        while i < j and j < len(nums):
            res.append(len(seen))

            seen[nums[i]] -= 1
            if seen[nums[i]] <= 0:
                del seen[nums[i]]

            i += 1

            seen[nums[j]] += 1

            j += 1

        res.append(len(seen))

        return res            
            
            

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.distinctNumbers

    check_solution_simple(
        sf,
        args=[[1,2,3,2,2,1,3], 3],
        expected=[3,2,2,2,3],
    )
