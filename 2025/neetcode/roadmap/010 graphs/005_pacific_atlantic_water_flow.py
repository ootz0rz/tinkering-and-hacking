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

'''
Rough idea:

From any given cell, we want to mark it valid if it a stream originating at it can reach both oceans.

We reach pacific iff
row <= -1, col <= -1

We reach atlantic iff
row >= nr, col >= nc

So need to find a path from each cell where both the above are true

----

We can start from the edges and move our way inwards, one for each ocean, and then look at intersection of reachable cells?
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        global _DIR

        nr = len(heights)        
        nc = len(heights[0])

        q = deque()
        valid = set()
        invalid = set()

        for ridx, row in enumerate(heights):
            for cidx, cell in enumerate(heights[ridx]):
                rc = (ridx, cidx)

                # already processed?
                if rc in valid:
                    continue

                if rc in invalid:
                    continue

                q.append(rc)

                # BFS
                while len(q) > 0:
                    r,c = q.popleft()

                    for x,y in _DIR:
                        rx = ridx + x
                        cy = cidx + y



        
        return list(valid)

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