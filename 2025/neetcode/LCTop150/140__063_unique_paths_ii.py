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

# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-interview-150
CLEAR = 0
BLOCK = 1
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        global CLEAR, BLOCK
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        mem = {} 

        def find(x, y):
            nonlocal obstacleGrid, mem, n, m

            if x < 0 or x >= n or y < 0 or y >= m:
                return 0 # out of bounds
            
            if not x in mem:
                mem[x] = {}
            
            if not y in mem[x]:
                val = 0
                if obstacleGrid[x][y] == BLOCK:
                    val = 0                
                elif x == (n - 1) and y == (m - 1):
                    val = 1
                else:
                    val = find(x + 1, y) + find(x, y + 1)

                mem[x][y] = val
            
            return mem[x][y]

        return find(0, 0)

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.uniquePathsWithObstacles

    check_solution_simple(
        sf,
        args=[[[0,0,0],[0,1,0],[0,0,0]]],
        expected=2,
    )
