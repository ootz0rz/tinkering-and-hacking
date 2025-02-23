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

# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = nums[0]
        count = 0

        # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        for n in nums:
            if count == 0:
                m = n
                count = 1
            elif m == n:
                count += 1
            else:
                count -= 1
        
        return m

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