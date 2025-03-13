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

# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

'''
Traverse until we find a "1", then consume them and count the number of islands as we go along

We'll mark visited squares in the grid by setting them to WATER as we go too, to avoid duplicates.
'''
DIR = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
LAND = "1"
WATER = "0"
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global DIR, LAND, WATER

        n = len(grid)
        m = len(grid[0])

        def consume(r, c):
            nonlocal grid
            # bounds check
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            
            # skip water
            if grid[r][c] == WATER:
                return
            
            # consume rest
            grid[r][c] = LAND
            for x, y in DIR:
                rx = x + r
                cy = y + c

                consume(rx, cy)
        
        num = 0 
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == LAND: # consume land we find
                    consume(r, c)
                    num += 1
        
        return num 

        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.numIslands

    check_solution_simple(  
        sf,
        args=[[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]],
        expected=1
    )