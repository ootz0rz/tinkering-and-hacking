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

# https://leetcode.com/problems/powx-n/description/

'''
Idea:

We can divide the exponent in half at each iteration to save on the number of multiplications we do
O(logn) instead of O(n)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:       
        def rec(x, n):
            if x == 0:
                return 0
            
            if n == 0:
                return 1
            
            res = rec(x * x, n // 2)
            
            return res if n % 2 == 0 else res * x
        
        res = rec(x, abs(n))
        return res if n >= 0 else (1/res)


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.myPow

    check_solution_simple(
        sf,
        args=[2, 10],
        expected=1024,
    )