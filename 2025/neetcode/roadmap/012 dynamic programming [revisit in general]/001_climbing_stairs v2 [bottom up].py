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

# https://neetcode.io/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        d = [1, 2]
        i = 3

        while i <= n:
            t = d[1]
            d[1] = d[0] + d[1]
            d[0] = t

            i = i + 1
        
        return d[1]

        
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