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
import sys

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('-inf')

        for n in nums:
            an = abs(n)
            ac = abs(closest)

            if (an < ac) or (an == ac and n > closest):
                closest = n
        
        return closest

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.findClosestNumber

    check_solution_simple(
        sf,
        args=[[0]],
        expected=0,
    )

    check_solution_simple(
        sf,
        args=[[1]],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[-1, 0, 1]],
        expected=0,
    )

    check_solution_simple(
        sf,
        args=[[-1, 10, 1]],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[2, -1, 1]],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[-4,-2,1,4,8]],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[2,1,1,-1,100000]],
        expected=1,
    )