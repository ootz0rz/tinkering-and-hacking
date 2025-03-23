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

# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/

'''
TYPE = [
    (nx, ny, {set of compatible types in this direction}), ...
]
'''
# (ROW, COL, {VALIDS})
_LEFT = (0, -1, {1, 4, 6})
_RIGHT = (0, 1, {1, 3, 5})
_UP = (-1, 0, {2, 3, 4})
_DOWN = (1, 0, {2, 5, 6})

_DIRS = {
    # X = left -1/right 1
    # Y = up -1/down 1
    1 : [_LEFT, _RIGHT], # left, right
    2 : [_UP, _DOWN], # up, down
    3 : [_LEFT, _DOWN], # left, down
    4 : [_DOWN, _RIGHT], # down, right
    5 : [_LEFT, _UP], # left, up
    6 : [_UP, _RIGHT], # up, right
}
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        global _DIRS

        n = len(grid)
        m = len(grid[0])

        goalx = n - 1
        goaly = m - 1

        q = deque([(0, 0)])
        visited = set()

        # O(n*m) runtime, O(n*m) space
        while len(q) > 0:

            # let's move one level at a time
            for _ in range(len(q)):
                xy = q.popleft()

                #print(f"{xy}={grid[xy[0]][xy[1]]} in {visited}? {xy in visited} ")

                # don't move backward
                if xy in visited:
                    continue
                
                visited.add(xy)
                x, y = xy

                # did we reach the end?
                if x == goalx and y == goaly:
                    return True # done !

                # these are the neighbours that we can possibly check
                for dx, dy, valids in _DIRS[grid[x][y]]:
                    # valid new cell?
                    xdx = x + dx
                    ydy = y + dy

                    #print(f"\t Valid? {xdx},{ydy} => {not (xdx < 0 or xdx >= n or ydy < 0 or ydy >= m)}")
                    if xdx < 0 or xdx >= n or ydy < 0 or ydy >= m:
                        continue
                    
                    # before we Q them up, make sure they can come back to us too
                    nType = grid[xdx][ydy]
                    #print(f"\t\tntype:{nType} in {valids}? {nType in valids}")
                    if not nType in valids:
                        continue
                    
                    # explore further
                    q.append((xdx, ydy))

        return False

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.hasValidPath

    check_solution_simple(
        sf,
        args=[[[1,1,2]]],
        expected=False,
    )

    check_solution_simple(
        sf,
        args=[[[1,2,1],[1,2,1]]],
        expected=False,
    )

    check_solution_simple(
        sf,
        args=[[[2,4,3],[6,5,2]]],
        expected=True,
    )