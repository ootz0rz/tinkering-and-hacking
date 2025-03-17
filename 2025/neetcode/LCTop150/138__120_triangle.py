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

# https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = {}
        def findMin(x, y):
            nonlocal triangle, m

            if x < 0 or x >= len(triangle) or y < 0 or y >= len(triangle[x]):
                return 0
            
            if not x in m:
                m[x] = {}

            if not y in m[x]:
                next1 = findMin(x + 1, y)
                next2 = findMin(x + 1, y + 1)
                
                m[x][y] = triangle[x][y] + min(next1, next2)
            
            return m[x][y]

        return findMin(0, 0)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minimumTotal

    check_solution_simple(
        sf,
        args=[[[2],[3,4],[6,5,7],[4,1,8,3]]],
        expected=11,
    )
