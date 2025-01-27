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