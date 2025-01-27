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

# https://neetcode.io/problems/islands-and-treasure

# valid directions
_DIR = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

_LAND = 2147483647
_WATER = -1
_TREASURE = 0

# DFS gets into an infinite loop here...
# we could maintain a grid of "visited" tiles to prevent this
# but the time complexity ends up being massive here
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        global _DIR, _LAND, _WATER, _TREASURE

        nr = len(grid)
        nc = len(grid[0])

        def mark(r, c, depth):
            nonlocal grid

            # check bounds
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return 
            
            # skip water
            g = grid[r][c]
            if g == _WATER:
                return 
            
            # mark depth
            grid[r][c] = min(g, depth)

            print(f"\t grid[{r}][{c}] = {grid[r][c]}")

            # mark neighbors as appropriate
            for x, y in _DIR:
                rx = r + x
                cy = c + y

                mark(rx, cy, depth + 1)

        for ridx, row in enumerate(grid):
            for cidx, cell in enumerate(row):
                if cell != _TREASURE:
                    continue
                
                # dfs from each Treasure
                print(f"Found treasure: {ridx},{cidx}")
                mark(ridx, cidx, 0)

        return grid


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.islandsAndTreasure

    grid = [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ]
    check_solution_simple(  
        sf,
        args=[grid],
        expected=grid
    )