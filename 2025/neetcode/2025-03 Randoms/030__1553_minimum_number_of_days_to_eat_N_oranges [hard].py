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

# https://leetcode.com/problems/path-with-maximum-gold/description/

class Solution:
    def minDays(self, n: int) -> int:
        
        d = {
            0: 0,
            1: 1,
        } 
        def sim(num: int):
            nonlocal d

            if num in d:
                return d[num]
            
            # add self, plus min of remainder
            d[num] = 1 + min(
                # n % 2/3 = number of 1-day eats that are leftover
                num % 2 + sim(num // 2),
                num % 3 + sim(num // 3)
            )

            return d[num]
        
        return sim(n)

                


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minDays

    check_solution_simple(
        sf,
        args=[0],
        expected=0,
    )

    check_solution_simple(
        sf,
        args=[1],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[2],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[3],
        expected=2,
    )

    check_solution_simple(
        sf,
        args=[5],
        expected=4,
    )

    check_solution_simple(
        sf,
        args=[10],
        expected=4,
    )