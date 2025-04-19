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
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def findMaxPath(sx, sy):
            nonlocal grid

            if not (0 <= sx < n) or not (0 <= sy < m):
                return 0

            if grid[sx][sy] == 0:
                return 0
            
            curGold = 0
            
            oldVal = grid[sx][sy]
            grid[sx][sy] = 0

            curGold = oldVal + max( #O(3^(mn)) since we can't revisit already visited cells
                curGold,
                findMaxPath(sx, sy + 1),
                findMaxPath(sx + 1, sy),
                findMaxPath(sx, sy - 1),
                findMaxPath(sx - 1, sy),
            )

            grid[sx][sy] = oldVal

            return curGold
        
        maxGold = 0
        for ridx in range(n):
            for cidx in range(m):
                maxGold = max(maxGold, findMaxPath(ridx, cidx))
        
        return maxGold
                


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.getMaximumGold

    check_solution_simple(
        sf,
        args=[[[0,6,0],[5,8,7],[0,9,0]]],
        expected=24,
    )