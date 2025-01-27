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

# https://neetcode.io/problems/count-number-of-islands

# valid directions
_DIR = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]

_LAND = "1"
_WATER = "0"

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global _DIR, _LAND, _WATER
        
        num = 0

        nr = len(grid)
        nc = len(grid[0])

        # search all positions around ourselves and mark them as
        # water
        def find_and_mark(r, c):
            nonlocal grid

            if r < 0 or r >= nr or c < 0 or c >= nc:
                return
            
            # print(f"\tfind and mark: r:{r} c:{c} => {grid[r][c]} -- {grid}")
            if grid[r][c] == _WATER:
                return
            
            grid[r][c] = _WATER
            for x, y in _DIR:
                rx = r + x
                cy = c + y

                find_and_mark(rx, cy)

        for ridx, row in enumerate(grid):
            for cidx, cell in enumerate(row):
                # skip water
                if cell == _WATER: 
                    continue
                
                # find extents of the land here
                # print(f"Found island start: {ridx} x {cidx}")
                find_and_mark(ridx, cidx)
                num = num + 1 # and mark our island
                # print(f"\t -> {grid}")

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

    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    check_solution_simple(  
        sf,
        args=[grid],
        expected=1
    )

    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    check_solution_simple(  
        sf,
        args=[grid],
        expected=4
    )