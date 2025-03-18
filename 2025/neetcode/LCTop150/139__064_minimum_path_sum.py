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

# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-interview-150
# DIR = [
#     (0, 1), # down
#     (1, 0), # right
# ]
DIR = [
    (0, -1), # up
    (-1, 0), # left
]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        global DIR 
        n = len(grid)
        m = len(grid[0])
        
        mem = {}
        
        def find(x, y):
            nonlocal grid, mem

            if x < 0 or x >= n or y < 0 or y >= m:
                print(f"\t\tINVALID XY: 0 > x:{x} >= {n} or 0 > y:{y} >= {m}")
                return -1 # we can safely use -1 since not a valid value otherwise
            
            print(f"find({x},{y})=>grid[{x},{y}]={grid[x][y]}")
            
            if not x in mem:
                mem[x] = {}

            if not y in mem[x]:
                a = find(x + 1, y)
                b = find(x, y + 1)

                mem[x][y] = grid[x][y]
                if a == -1 and b >= 0:
                    mem[x][y] += b
                    print(f"\tCALC XY:{x},{y} = {mem[x][y]} <= grid[x][y] + b = {grid[x][y]} + {b}")
                elif a >= 0 and b == -1:
                    mem[x][y] += a
                    print(f"\tCALC XY:{x},{y} = {mem[x][y]} <= grid[x][y] + a = {grid[x][y]} + {a}")
                elif a >= 0 and b >= 0:
                    mem[x][y] += min(a, b)
                    print(f"\tCALC XY:{x},{y} = {mem[x][y]} <= grid[x][y] + min(a,b) = {grid[x][y]} + min({a}, {b})")
                else:
                    print(f"\tCALC XY:{x},{y} = {mem[x][y]} <= grid[x][y] = {grid[x][y]}")
            else:
                print(f"\tMEM XY:{x},{y} = {mem[x][y]}")

            return mem[x][y]

        r = find(0, 0)
        import pprint; pprint.pprint(mem)
        return r

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))

    from TestHarness import *

    s = Solution()
    sf = s.minPathSum

    check_solution_simple(
        sf,
        args=[[[1,3,1],[1,5,1],[4,2,1]]],
        expected=7,
    )
