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

# https://leetcode.com/problems/find-the-longest-equal-subarray/description/

EMPTY = "."
WALL = "+"

DIRS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        global EMPTY, WALL, DIRS

        n = len(maze)
        m = len(maze[0])

        se = (tuple(entrance))

        q = deque([(se, 0)])

        # BFS path find
        pathLen = None
        while len(q) > 0:
            #print(f"path: {pathLen} |||| v: {v} |||| Q: {q}")
            xy, dist = q.popleft()
            x, y = xy 

            #print(f"\t -> {xy} = {dist}")

            # valid?
            if not (0 <= x < n) or not (0 <= y < m):
                #print(f"\t\t Invalid {xy}")
                continue
            
            # can't pass walls
            if maze[x][y] == WALL:
                #print(f"\t\t WALL {xy}")
                continue

            # is this an exit?
            if ((x == 0 or x == n-1) or (y == 0 or y == m-1)) and xy != se:
                pathLen = min(pathLen, dist) if pathLen is not None else dist
                #print(f"\t\t EXIT {xy}, new path: {pathLen}")
                continue # NOTE we could also just exit early here, since we use BFS, first match will be shortest
            
            # explore neighbours
            maze[x][y] = WALL
            for dx, dy in DIRS:
                xdx = x + dx 
                ydy = y + dy
                
                q.append(((xdx, ydy), dist + 1))
        
        return pathLen if pathLen is not None else -1

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.nearestExit

    check_solution_simple(
        sf,
        args=[[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2]],
        expected=1,
    )

    check_solution_simple(
        sf,
        args=[[["+","+","+"],[".",".","."],["+","+","+"]], [1,0]],
        expected=2,
    )
