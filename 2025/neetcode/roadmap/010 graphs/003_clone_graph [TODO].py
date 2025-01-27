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

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        global _EMPTY, _FRUIT, _ROT

        nr = len(grid)
        nc = len(grid[0])

        q = deque() # [tuple(x,y), ...]
        visited = set() # [tuple((x, y)), ...]

        def add_node_to_visit(r, c):
            nonlocal grid
            # check bounds
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return 
            
            # check if we've visited this node already
            rc = (r, c)
            if rc in visited:
                return
            
            # skip water and other treasure
            g = grid[r][c]
            if g == _WATER or g == _TREASURE:
                return
            
            q.append(rc)
            visited.add(rc)

        # seed all the treasure boxes, O(m x n)
        for ridx, row in enumerate(grid):
            for cidx, cell in enumerate(row):
                if cell != _TREASURE:
                    continue
                
                # bfs from each Treasure
                rc = (ridx, cidx)
                print(f"Found treasure: {rc}")
                q.append(rc)
                visited.add(rc)

        # start BFS.. we'll process all nodes in our Q at same time
        # before starting the next batch of things we've added on
        # this iteration
        #
        # by doing this, we explore as BFS from each treasure at the "same" time
        # and avoid doing extra overlapping work
        #
        # finally, we track the distance at each iteration and mark that on our grid
        # as appropriate
        dist = 0
        while len(q) > 0:

            for _ in range(len(q)):
                r, c = q.popleft() # we're gonna be adding new nodes to the end of our Q, so FIFO
                
                grid[r][c] = dist # mark our distance

                # iterate on neighbours
                for x, y in _DIR:
                    rx = r + x
                    yc = y + c
                    
                    add_node_to_visit(rx, yc)

            # inc distance for next iteration
            dist = dist + 1

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