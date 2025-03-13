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

# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

'''
Traverse until we find a "1", then consume them and count the number of islands as we go along

We'll mark visited squares in the grid by setting them to WATER as we go too, to avoid duplicates.
'''
DIR = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]
X = "X"
O = "O"

SURR = "-"
# doesn't work
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        global DIR, X, O, SURR

        n = len(board)
        m = len(board[0])

        def Xindir(x, y, dx, dy):
            xdx = x + dx
            ydy = y + dy

            if (
                xdx < 0
                or ydy < 0
                or xdx >= n 
                or ydy >= m
            ):
                return False 
            
            return board[xdx][ydy] == X or board[xdx][ydy] == SURR or Xindir(xdx, ydy, dx, dy)
        
        for x in range(n):
            for y in range(m):
                if board[x][y] == O:
                    surrounded = True 
                    for dx, dy in DIR:
                        surrounded = surrounded and Xindir(x, y, dx, dy)
                        if not surrounded:
                            break 
                    
                    if surrounded:
                        board[x][y] = SURR

        for x in range(n):
            for y in range(m):
                if board[x][y] == SURR:
                    board[x][y] = X 

        return board # for easier testing
        
        

if __name__ == '__main__':
    # stupid...but works
    import sys, os

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(SCRIPT_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(SCRIPT_DIR))) # parent

    from TestHarness import *

    s = Solution()
    sf = s.numIslands

    check_solution_simple(  
        sf,
        args=[[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]],
        expected=1
    )