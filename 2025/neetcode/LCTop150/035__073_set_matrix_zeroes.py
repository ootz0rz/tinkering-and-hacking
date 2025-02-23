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

# https://leetcode.com/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
'''
Idea:

At first, feels like we can just DFS but then would have to track visited nodes to make sure we don't repeat work or do extra work

So instead gonna do a pass, track which nodes to start with, and dfs from those to mark as 0 until we hit another 0
'''
_DIR = [
    (0, 1),
    (-1, 0),
    (1, 0),
    (0, -1),
]
_MATCHER = 0
# O(m*n) run, but O(m*n) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        global _MATCHER, _DIR

        nodes = set()
        n = len(matrix)
        m = len(matrix[0])

        def zPath(x, y, dx, dy):
            nonlocal matrix, n, m
            
            while (x >= 0 and x < n) and (y >= 0 and y < m): # and matrix[x][y] != _MATCHER:
                print(f"\t\t -> SET {x},{y} = 0")
                matrix[x][y] = _MATCHER
                x += dx 
                y += dy
        
        # find our starter nodes
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == _MATCHER:
                    print(f"Found: {i},{j}")
                    nodes.add((i, j))
        
        # start zero out in each direction
        for x, y in nodes:
            print(f"Start {x},{y}")
            for dx, dy in _DIR:
                print(f"\t -> DIR: {dx},{dy}")
                zPath(x+dx, y+dy, dx, dy)
        
        return matrix


if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.setZeroes

    check_solution_simple(  
        sf,
        args=[[[1,1,1],[1,0,1],[1,1,1]]],
        expected=[[1,0,1],[0,0,0],[1,0,1]]
    )

    check_solution_simple(  
        sf,
        args=[[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]],
        expected=[[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    )
