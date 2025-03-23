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

# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        large = [-9999, -9999, -9999] # largest, 2nd largest, 3rd largest
        
        # NOTE: We have to track 2 smallest as well, in case they're abs() large and
        #       both negative, they might multiply to a larger value
        small = [9999, 9999] # smallest, 2nd smallest

        for n in nums:

            if n > large[0]:
                large[2] = large[1]
                large[1] = large[0]
                large[0] = n
            elif n > large[1]:
                large[2] = large[1]
                large[1] = n
            elif n > large[2]:
                large[2] = n

            if n < small[0]:
                small[1] = small[0]
                small[0] = n
            elif n < small[1]:
                small[1] = n
        
        return max(large[0] * large[1] * large[2], small[0] * small[1] * large[0])

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findPairs

    check_solution_simple(
        sf,
        args=[[3,1,4,1,5], 2],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[[1,2,3,4,5], 1],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[[1,3,1,5,4], 0],
        expected=1,
    )