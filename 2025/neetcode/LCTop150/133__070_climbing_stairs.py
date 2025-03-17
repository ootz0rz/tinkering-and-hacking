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

# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}

        def gen(steps):
            if steps <= 2:
                return steps
            
            if not steps in m:
                m[steps] = gen(steps - 1) + gen(steps - 2)

            return m[steps]

        return gen(n)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.climbStairs

    check_solution_simple(
        sf,
        args=[2],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[3],
        expected=3,
    )