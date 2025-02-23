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

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
'''
Two pointers...

Start on both ends.

If LS + RS > t, RS--. If LS + RS < t, LS++. Else, we found our match.
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            el = numbers[l]
            er = numbers[r]

            s = el + er
            if s == target:
                break

            if s > target:
                r -= 1
            else:
                l += 1
        
        return [l + 1, r + 1]

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.twoSum

    check_solution_simple(  
        sf,
        args=[[2,7,11,15], 9],
        expected=[1, 2]
    )
