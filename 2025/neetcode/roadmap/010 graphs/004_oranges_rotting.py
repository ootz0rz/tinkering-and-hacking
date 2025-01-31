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

_EMPTY = 0
_FRUIT = 1
_ROT = 2

'''
Rough idea:

Go through and count number of fruit. Mark all rotting fruit in Q.

BFS on the Q one level at a time. Track depth as "minTime"

If we reach all the fruit while doing this, we return minTime. Otherwise, -1
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        global _EMPTY, _FRUIT, _ROT

        nr = len(grid)        
        nc = len(grid[0])

        q = deque() # [tuple(x,y), ...]
        visited = set() # [tuple((x, y)), ...]

        minTime = 0
        numFruit = 0

        def add_to_visit(r, c):
            nonlocal numFruit

            # check bounds
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return 
            
            # skip visited
            rc = (r,c)
            if rc in visited:
                return
            
            # skip empty
            g = grid[r][c]
            if g != _FRUIT:
                return 
            
            # visit next round
            q.append(rc)
            visited.add(rc)

            numFruit -= 1

        # find the rotting fruit and begin BFS from there.
        # will assume there can be multiple of these which spread their 'rotting' at the same time
        #
        # we also count the num of FRUIT to make sure we get to all of them
        for ridx, row in enumerate(grid):
            for cidx, cell in enumerate(row):
                if cell == _FRUIT:
                    numFruit += 1
                elif cell == _ROT:
                    rc = (ridx, cidx)

                    q.append(rc)
                    visited.add(rc)

        # now begin to process as BFS
        while numFruit > 0 and len(q) > 0:

            # pop all we have in Q so far and visit the neighbours
            for _ in range(len(q)):
                r,c = q.popleft() # fifo

                # check neighbours
                for x, y in _DIR:
                    rx = r + x
                    cy = c + y

                    add_to_visit(rx, cy)
            
            minTime += 1 # 0 at first, if all we have is rotting fruit

        if numFruit == 0:
            return minTime

        return -1


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.orangesRotting

    grid = [[1,1,0],[0,1,1],[0,1,2]]
    check_solution_simple(  
        sf,
        args=[[[0]]],
        expected=0
    )

    grid = [[1,1,0],[0,1,1],[0,1,2]]
    check_solution_simple(  
        sf,
        args=[grid],
        expected=4
    )